from flask import Flask, request, jsonify, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Feedback
from forms import NewUserForm, UserForm, ReviewForm
from sqlalchemy.exc import IntegrityError
from random import randint
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedback_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def root():
    """Show homepage with links to site areas."""
    return redirect('/reviews')


@app.route('/reviews')
def homepage():
    reviews = Feedback.query.order_by(
        Feedback.created_at.desc()).limit(25).all()
    users = User.query.all()
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    else:
        return render_template('homepage.html', users=users, reviews=reviews, title='stupid reviews')


# auth routes


@app.route('/register', methods=['get', 'post'])
def register_user():
    form = NewUserForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        new_user = User.register(
            first_name, last_name, username, password, email)
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('username taken')
            return render_template('users/user_register.html', form=form, title='register user')
        session['user_id'] = new_user.id
        return redirect('/reviews')
    else:
        return render_template('users/user_register.html', form=form, title='register user')


@app.route('/login', methods=['get', 'post'])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            flash(f'welcome back {user.username}', 'success')
            session['user_id'] = user.id
            return redirect('/reviews')
        else:
            form.username.errors = ['invalid username or password']
    else:
        return render_template('users/user_login.html', form=form, title='login user')


@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""
    session.pop("user_id")
    flash('goodbye', 'success')
    return redirect("/login")


# user routes


@app.route('/users')
def users_page():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('/users/users_index.html', users=users, title='new user form')


@app.route('/users/new')
def create_user():
    '''shows new user page'''
    return render_template('/users/new_user.html', title='new user form')


@app.route('/users/new', methods=['post'])
def new_user_form():
    '''shows new user form page'''
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')


@app.route("/users/<int:user_id>")
def find_user(user_id):
    '''show details about a single pet'''
    user = User.query.get_or_404(user_id)
    reviews = Feedback.query.order_by(Feedback.created_at.desc()).all()
    return render_template('/users/user_details.html', user=user, reviews=reviews, title='user details')


@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('/users/edit_user.html', user=user, title='edit user form')


@app.route('/users/<int:user_id>/delete', methods=["post"])
def delete_user(user_id):
    """Handle form submission for deleting an existing user"""
    user = User.query.get_or_404(user_id)
    if user.id == session['user_id']:
        db.session.delete(user)
        db.session.commit()
        flash('user deleted', 'info')
        return redirect('/')
    else:
        flash('do not have required permissions', 'error')
        return redirect('/')


# tweet routes


@app.route('/reviews/<int:id>')
def show_review(id):
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    review = Feedback.query.get_or_404(id)
    return render_template('reviews/review_details.html', review=review, title='review info')


@app.route('/users/<int:user_id>/reviews/new', methods=['get', 'post'])
def review_new_form(user_id):
    """Show a form to create a new tweet for a specific user"""
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    user = User.query.get_or_404(user_id)
    form = ReviewForm()
    if form.validate_on_submit():
        new = Feedback(
            title=form.title.data,
            content=form.content.data,
            username=user.username
        )
        db.session.add(new)
        db.session.commit()

        flash('review created!', 'success')
        return redirect(f"/users/{user_id}")
    else:
        return render_template("/reviews/new_review.html", form=form, user=user, title='provide feedback')


@app.route('/users/<int:user_id>/reviews/new', methods=["post"])
def reviews_new(user_id):
    """Handle form submission for creating a new review for a specific user"""
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    user = User.query.get_or_404(user_id)
    new_review = Feedback(title=request.form['title'],
                          content=request.form['content'],
                          user=user)

    db.session.add(new_review)
    db.session.commit()
    flash(f"Feedback '{new_review.title}' added.", 'success')
    return redirect(f"/users/{user_id}")


@app.route('/reviews/<int:id>/edit', methods=['get'])
def edit_review_form(id):
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    review = Feedback.query.get_or_404(id)
    form = ReviewForm(obj=review)
    if form.validate_on_submit():
        db.session.commit()
    else:
        return render_template('reviews/edit_review.html', form=form, review=review, title='review info')


@app.route('/reviews/<int:id>/edit', methods=['get', 'post'])
def edit_tweet(id):
    """Handle form submission for creating a new tweet for a specific user"""
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    if 'user_id' in session:
        review = Feedback.query.get_or_404(id)
        form = ReviewForm(obj=review)
        if form.validate_on_submit():
            review.title = form.title.data
            review.content = form.content.data
            db.session.commit()
            flash('Feedback updated!', 'success')
            return redirect('/')
        else:
            return render_template('reviews/tweet_details.html', review=review, form=form, title='review info')


@app.route('/reviews/<int:review_id>/delete', methods=['post'])
def delete_tweet(review_id):
    review = Feedback.query.get_or_404(review_id)
    if 'user_id' not in session:
        flash('please login first', 'error')
        return redirect('/login')
    if review.user.id == session['user_id']:
        db.session.delete(review)
        db.session.commit()
        flash('review deleted', 'info')
        return redirect('/')
    else:
        flash('do not have required permissions', 'error')
        return redirect('/')
