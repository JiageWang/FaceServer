from wtforms import Form, IntegerField, StringField
from wtforms.validators import NumberRange, Length
import datetime


class RecordSearchForm(Form):
    start = '20190616'
    end = str(datetime.date.today()).replace('-', '')
    default_time = start+'_'+end
    time = StringField(validators=[Length(17)], default=default_time)
    device = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
