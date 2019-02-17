from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name= StringField('name', validators=[DataRequired()])
    email= StringField('email', validators=[DataRequired(), Email()])
    subject= StringField('subject', validators=[DataRequired()])


# Your form should have a text field for name, email,
# subject and a text area for a message. Also remember to
# protect your form with a CSRF token. 