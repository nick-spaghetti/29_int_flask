
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = 'https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg'


def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """cupcake Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, unique=True, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    img = db.Column(db.String, nullable=True, default=GENERIC_IMAGE)
    image = db.relationship('Image', uselist=False, backref='cupcake')

    def serialize(self):
        """Returns a dict representation of todo which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'img': self.img,
        }

    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} >"

    def image(self):
        """Return image for pet -- bespoke or generic."""

        return self.img or GENERIC_IMAGE


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)
    cup_id = db.Column(db.Integer, db.ForeignKey(
        'cupcakes.id'), nullable=True)
    cup = db.relationship('Cupcake', backref='image')

# app.py
