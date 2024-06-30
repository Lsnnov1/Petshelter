from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""
    name = StringField("Enter pet name", validators=[InputRequired(message="Enter animal name")])
    species = RadioField("Enter pet species", choices=[
        ('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine','Porcupine')], validators=[InputRequired(message="Select animal species")])
    photo_url = StringField("Photo url link", validators=[Optional()])
    age = IntegerField("Enter pet age", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    name = StringField("Enter pet name", validators=[InputRequired(message="Enter animal name")])
    species = RadioField("Enter pet species", choices=[
        ('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine','Porcupine')], validators=[InputRequired(message="Select animal species")])
    photo_url = StringField("Photo url link", validators=[Optional()])
    age = IntegerField("Enter pet age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")
    submit = SubmitField("Update Pet")

    