
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import NewCupForm, EditCupForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def root():
    return redirect('/api/cupcakes')


@app.route('/api/cupcakes', methods=['get'])
def index():
    cupcakes = [cupcake.serialize()
                for cupcake in Cupcake.query.order_by(Cupcake.rating.desc()).all()]
    return render_template('index.html', cupcakes=cupcakes, title='index')


@app.route("/api/cupcakes/new", methods=["get", "post"])
def new_cup_form():
    form = NewCupForm()

    if form.validate_on_submit():
        new_cup = Cupcake(
            flavor=form.flavor.data,
            rating=form.rating.data,
            size=form.size.data,
            image=form.image.data
        )

        db.session.add(new_cup)
        db.session.commit()

        flash('Cupcake created!')
        return redirect('/')
    else:
        return render_template("/forms/new_cupcake.html", form=form, title='add a cupcake')


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    # cupcake = Cupcake.query.get_or_404(id)
    # return jsonify(cupcake=cupcake.serialize())
    cupcake = Cupcake.query.get_or_404(id)
    form = EditCupForm(obj=cupcake)
    return render_template('info.html', cupcake=cupcake, form=form, title='cupcake info')
    # raise


@app.route("/api/cupcakes/<int:id>", methods=['get', 'post'])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    form = EditCupForm(obj=cupcake)

    if form.validate_on_submit():
        cupcake.flavor = form.flavor.data
        cupcake.rating = form.rating.data
        cupcake.size = form.size.data
        db.session.commit()
        flash('Cupcake updated!')
        return redirect('/')
    else:
        return render_template('info.html', cupcake=cupcake, form=form, title='cupcake info')


@app.route("/api/cupcakes/<int:id>", methods=["delete"])
def remove_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    flash('Cupcake deleted!')
    return redirect('/')
