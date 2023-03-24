from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import datetime


db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Site user."""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20),
                         nullable=False,
                         unique=True)
    password = db.Column(db.Text,
                         nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    reviews = db.relationship("Feedback", backref="user",
                              cascade="all, delete-orphan")

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        '''register user with hashed password and return user'''
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name, )

    @classmethod
    def authenticate(cls, username, pwd):
        '''validate that user exists and pwd is correct
        return user if valid; else return false
        '''
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False

    def greet(self):
        '''greet using name'''
        return f"Hi, {self.username}"


class Feedback(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=True, default='title')
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.now)
    username = db.Column(db.String(20), db.ForeignKey(
        'users.username'), nullable=False)

    users = db.relationship(
        'User',
        backref="review",
    )

    @property
    def date_time(self):
        return self.created_at.strftime('%a %b %-d %Y, %-I:%M %p')

    def __repr__(self):
        '''show info about user'''
        p = self
        return f"<id: {p.id} title: {p.title} content: {p.content} created_at: {p.created_at} user_id: {p.user.username}>"
