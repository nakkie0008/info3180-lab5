from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    ttitle = StringField('Movie Title', validators=[InputRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(min=10, max=500)])
    poster = FileField('Movie Poster', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')