from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import InputRequired


class NewCupForm(FlaskForm):
    flavor = StringField(label='flavor', name='flavor',
                         validators=[InputRequired()])
    size = StringField(label='size', name='size',
                       validators=[InputRequired()])
    rating = IntegerField(label='rating', name='rating')
    # img = FileField(label='image', name='image')


class EditCupForm(FlaskForm):
    flavor = StringField(label='flavor', name='flavor',
                         validators=[InputRequired()])
    size = StringField(label='size', name='size',
                       validators=[InputRequired()])
    rating = IntegerField(label='rating', name='rating')
    # img = FileField(label='image', name='image')
