from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Do you believe in luck? Yes or No', validators=[DataRequired()])
    submit = SubmitField('Start Game')

class GameForm(FlaskForm):
    play = SubmitField('Play')
    play_again = SubmitField('Play Again')
    quit = SubmitField('Quit')