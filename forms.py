from flask.ext.wtf import Form, SelectField


class TestForm(Form):
    make = SelectField(u'', choices=())
    model = SelectField(u'', choices=())
