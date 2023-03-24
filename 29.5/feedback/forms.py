from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, length


class NewUserForm(FlaskForm):
    first_name = StringField(label='first name', validators=[InputRequired()])
    last_name = StringField(label='last name', validators=[InputRequired()])
    email = StringField(label='email', validators=[
                        InputRequired(), length(max=50)])
    username = StringField(label='username', validators=[InputRequired()])
    password = PasswordField(label='password', validators=[InputRequired()])


class UserForm(FlaskForm):
    username = StringField(label='username', validators=[InputRequired()])
    password = PasswordField(label='password', validators=[InputRequired()])


class ReviewForm(FlaskForm):
    title = StringField(label='title')
    content = TextAreaField(label='content', validators=[length(max=400)])
