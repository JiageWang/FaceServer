from wtforms import Form, IntegerField, FileField, StringField
from wtforms.validators import NumberRange, DataRequired, Length


class RegisterForm(Form):
    img = FileField(validators=[DataRequired()])
    name = StringField(validators=[Length(1, 20), DataRequired()])
    number = IntegerField(validators=[NumberRange(0, 59999999)])
    branch = StringField(validators=[Length(0, 50)], default='新凤鸣')
    duty = StringField(validators=[Length(0, 50)], default='员工')

