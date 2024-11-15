def process_employee_data(employee_records):
    # Initialize a dictionary to store salary totals and counts for each department
    department_salaries = {}
    
    # Process each employee record
    for employee in employee_records:
        department = employee['department']
        salary = employee['salary'] 
        
        # Initialize the department data if not already present
        if department not in department_salaries:
            department_salaries[department] = {'total_salary': 0, 'employee_count': 0}
        
        # Update the department's total salary and employee count
        department_salaries[department]['total_salary'] += salary
        department_salaries[department]['employee_count'] += 1
    
    # Prepare the result with total and average salaries
    result = {}
    for department, data in department_salaries.items():
        total_salary = data['total_salary']
        employee_count = data['employee_count']
        average_salary = total_salary / employee_count if employee_count > 0 else 0
        result[department] = {'total_salary': total_salary, 'average_salary': average_salary}
    
    return result

# Function to take user input for employee records
def get_employee_data():
    employee_records = []
    print("Enter employee details (type 'done' to finish):")
    
    while True:
        name = input("Enter employee name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        department = input("Enter employee department: ")
        salary = float(input("Enter employee monthly salary: "))
        
        # Append the employee record as a dictionary to the list
        employee_records.append({
            'name': name,
            'department': department,
            'salary': salary
        })
    
    return employee_records

# Get data from the user
employee_records = get_employee_data()

# Call the function to process data and print the result
result = process_employee_data(employee_records)
print(result)
