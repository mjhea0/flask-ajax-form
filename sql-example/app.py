import json
from flask import Flask, request, render_template, make_response
from form import TestForm
from data import DEPARTMENT_LIST, EMPLOYEE_LIST

app = Flask(__name__)
app.config['SECRET_KEY'] = "my precious"


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render form and handle form submission
    """
    form = TestForm(request.form)
    form.department.choices = [('', 'Select a department')] + [
        (x['department_id'], x['name']) for x in DEPARTMENT_LIST]
    chosen_department = None
    chosen_employee = None
    
    return render_template('index.html', form=form)


@app.route("/<int:department_id>/", methods=["GET"])
def get_request(department_id):
    """
    Handle GET request to - /<department_id>/
    Return a list of tuples - (<employee id>, <employee name>)
    """
    data = [
        (x['employee_id'], x['name']) for x in EMPLOYEE_LIST
        if x['department_id'] == department_id]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)
