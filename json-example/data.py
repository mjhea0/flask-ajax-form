import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)
pprint(data["departments"])
print type(data["departments"])


DEPARTMENT_LIST = (
    {'department_id': 1, 'name': 'Accounting'},
    {'department_id': 2, 'name': 'Sales'},
    {'department_id': 3, 'name': 'Management'},
)

print(DEPARTMENT_LIST)

# EMPLOYEE_LIST = (
#     {'employee_id': 1, 'department_id': 1, 'name': 'Kyra Davis'},
#     {'employee_id': 2, 'department_id': 1, 'name': 'Abigail Whitfield'},
#     {'employee_id': 3, 'department_id': 1, 'name': 'Maya Chase'},
#     {'employee_id': 4, 'department_id': 1, 'name': 'Lydia Hyde'},
#     {'employee_id': 5, 'department_id': 2, 'name': 'Wynne Erickson'},
#     {'employee_id': 6, 'department_id': 2, 'name': 'Candice Davidson'},
#     {'employee_id': 7, 'department_id': 2, 'name': 'Lawrence Roman'},
#     {'employee_id': 8, 'department_id': 2, 'name': 'Kameko Parker'},
#     {'employee_id': 9, 'department_id': 3, 'name': 'Jamal Everett'},
#     {'employee_id': 10, 'department_id': 3, 'name': 'Avram Burks'},
#     {'employee_id': 11, 'department_id': 3, 'name': 'Mia Mendez'},
#     {'employee_id': 12, 'department_id': 3, 'name': 'Ila Cantrell'},
# )













