import json
from flask import Flask, request, render_template, make_response
from form import TestForm
from data import MAKE_LIST, MODEL_LIST

app = Flask(__name__)
app.config['SECRET_KEY'] = "illnevertell"


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render form and handle form submission
    """
    form = TestForm(request.form)
    form.make.choices = [('', '--- Select One ---')] + [
        (x['make_id'], x['name']) for x in MAKE_LIST]
    chosen_make = None
    chosen_model = None
    
    return render_template('index.html', form=form)


@app.route("/<int:make_id>/", methods=["GET"])
def get(make_id):
    """
    Handle GET request to /<make_id>/
    Return a list of 2-tuples (<model id>, <model name>)
    """
    data = [
        (x['model_id'], x['name']) for x in MODEL_LIST
        if x['make_id'] == make_id]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)
