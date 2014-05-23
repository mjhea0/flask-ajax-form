from flask.ext.wtf import Form, SelectField


class TestForm(Form):
    department = SelectField(u'', choices=())
    employee = SelectField(u'', choices=())
