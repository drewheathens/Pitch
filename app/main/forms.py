from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField,TextAreaField
from wtforms.validators import ValidationError, DataRequired


class Post(FlaskForm):
    post = TextAreaField(('Say something'), validators=[DataRequired()])
    category = SelectField('Category', choices=[('Pickuplines','Pickuplines'),('Technology','Technology'),('BusinessPitch','Business Pitch'),('Sales','Sales'),('Interview','Interview')])

    submit = SubmitField(('Submit'))

class Comment(FlaskForm):
    details = StringField('Write a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')