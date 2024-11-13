# Employee 1
employee_1 = {
    "id": "1",
    "name": "David Wallace",
    "job title": "CFO",
    "shift": "9am to 5pm",
    "salary": "30,000"
}

# Employee 2
employee_2 = {
    "id": "2",
    "name": "Charles Miner",
    "job title": "Vice President",
    "shift": "9am to 5pm",
    "salary": "22,000"
}

# Employee 3
employee_3 = {
    "id": "3",
    "name": "Michael Scott",
    "job title": "Regional Manager",
    "shift": "9am to 5pm",
    "salary": "10,000"
}

# Employee 4
employee_4 = {
    "id": "4",
    "name": "Jim Halpert",
    "job title": "Sales Representative",
    "shift": "9am to 6pm",
    "salary": "8,000"
}

# Employee 5
employee_5 = {
    "id": "5",
    "name": "Pam Halpert",
    "job title": "Sales Representative",
    "shift": "9am to 5pm",
    "salary": "8,000"
}

# Employee 6
employee_6 = {
    "id": "6",
    "name": "Dwight Schrute",
    "job title": "Sales Representative",
    "shift": "9am to 5pm",
    "salary": "8,000"
}

# Employee 7
employee_7 = {
    "id": "7",
    "name": "Angela Martin",
    "job title": "Senior Accountant",
    "shift": "9am to 5pm",
    "salary": "8,000"
}

# Employee 8
employee_8 = {
    "id": "8",
    "name": "Kelly Kapoor",
    "job title": "Customer Service Representative",
    "shift": "9am to 5pm",
    "salary": "7,000"
}

# Employee 9
employee_9 = {
    "id": "9",
    "name": "Erin Hannon",
    "job title": "Receptionist",
    "shift": "9am to 5pm",
    "salary": "5,500"
}

# Employee 10
employee_10 = {
    "id": "10",
    "name": "Darryl Philbin",
    "job title": "Warehouse Foreman",
    "shift": "9am to 5pm",
    "salary": "9,500"
}

employees = [employee_1, employee_2, employee_3, employee_4, employee_5, employee_6, employee_7, employee_8, employee_9, employee_10]

for employee in employees:
    print(f"ID: {employee.get('id')}, Name: {employee.get('name')}, Job Title: {employee.get('job title')}, Shift: {employee.get('shift')}, Salary: {employee.get('salary')}, ")