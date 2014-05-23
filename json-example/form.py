from flask.ext.wtf import Form
from wtforms import SelectField


class TestForm(Form):
    department = SelectField(u'', choices=())
    employee = SelectField(u'', choices=())