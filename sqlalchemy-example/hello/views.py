import json
from flask import Flask, request, render_template, make_response
from form import TestForm
from hello import app, db
from models import Department, Employee

@app.route("/department", methods=["GET", "POST"])
def index():
    """
    Render form and handle form submission
    """
    form = TestForm(request.form)
    departments = Department.query.all()
    form.department.choices = [('', 'Select a department')] + [
        (department.id, department.name) for department in departments]
    chosen_department = None
    chosen_employee = None
    
    return render_template('index.html', form=form)


@app.route("/department/<int:department_id>/", methods=["GET"])
def get_request(department_id):
    """
    Handle GET request to - /<department_id>/
    Return a list of tuples - (<employee id>, <employee name>)
    """
    employees = Employee.query.all()

    data = [
        (employee.id, employee.name) for employee in employees 
        if employee.department_id == department_id
    ]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response