""" Task-2 Scripting """

import csv

def calculate_average_salary(department):
    # Calculates the average monthly salary for a given department
    total_salary = 0
    num_employees = 0

    # Iterate over employees in the department and sum their salaries
    for employee in department:
        total_salary += float(employee['MONTHLY_SALARY'])
        num_employees += 1

    # Check if there are employees in the department to avoid division by zero
    if num_employees > 0:
        return total_salary / num_employees
    else:
        return 0

def generate_report():
    departments = {}  # Dictionary to store departments and their employees

    # Read and process employees.csv
    with open('employees.csv', 'r') as employees_file:
        employees = csv.DictReader(employees_file)
        for employee in employees:
            department_id = employee['DEPT_ID']

            # Create a list for each department and append employees to it
            if department_id not in departments:
                departments[department_id] = []
            departments[department_id].append(employee)

    # Read and process salaries.csv
    with open('salaries.csv', 'r') as salaries_file:
        salaries = csv.DictReader(salaries_file)
        for salary in salaries:
            department_id = salary['DEPT_ID']

            # Assign the monthly salary to each employee in the corresponding department
            if department_id in departments:
                for employee in departments[department_id]:
                    employee['MONTHLY_SALARY'] = salary['MONTHLY_SALARY']

    department_salaries = []  # List to store department IDs and average salaries
    for department_id, department in departments.items():
        # Calculate the average monthly salary for each department
        average_salary = calculate_average_salary(department)
        department_salaries.append({'DEPT_ID': department_id, 'AVG_MONTHLY_SALARY': average_salary})

    # Sort departments based on average monthly salary in descending order
    department_salaries.sort(key=lambda x: x['AVG_MONTHLY_SALARY'], reverse=True)

    # Print the top 3 departments along with their average monthly salaries
    for department in department_salaries[:3]:
        print(f"{department['DEPT_ID']}\n{department['AVG_MONTHLY_SALARY']} (USD)\n")

# Run the script
generate_report()



