from wtforms import Form, IntegerField, FileField
from wtforms.validators import NumberRange, DataRequired


class FaceForm(Form):
    device = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
    img = FileField(validators=[DataRequired()])
