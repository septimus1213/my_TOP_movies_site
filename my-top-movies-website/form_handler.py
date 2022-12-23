from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange


# ---- WTForms SECTION --------- #
class UpdateRating(FlaskForm):
    review_field = StringField(label="New review", validators=[DataRequired()])
    rating_field = FloatField(label="New rating", validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
    submit = SubmitField(label="Done")

class AddMovie(FlaskForm):
    search = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add movie")
# ------------------------------ #