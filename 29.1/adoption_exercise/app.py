from flask import Flask, url_for, render_template, redirect, flash, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm
# import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def root():
    return redirect('/pets')


@app.route('/pets')
def list_pets():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('index.html', pets=pets, title='pet index')


@app.route("/new", methods=["get", "post"])
def add_pet():
    form = NewPetForm()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))
    else:
        return render_template("/forms/new_pet.html", form=form, title='new pet form')


@app.route('/pets/<int:pet_id>/edit', methods=['get', 'post'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))
    else:
        return render_template("/forms/pet_edit_form.html", form=form, pet=pet, title='edit pet info')


# @app.route('/upload', methods=['get'])
# def upload():
#     return render_template('upload.html')


# @app.route('/upload', methods=['post'])
# def upload_form():
#     image = request.files['image']
#     img = Image(data=base64.b64encode(image.read()))
#     db.session.add(img)
#     db.session.commit()
#     return 'Image uploaded successfully'
