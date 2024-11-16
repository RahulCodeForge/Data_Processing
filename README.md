# Data Processing

This Python project processes employee data to calculate salary information by department. It takes a list of employee records, each containing an employee’s name, department, and monthly salary, and calculates:

- The total salary expense for each department
- The average salary per department

The program also ensures that all departments are represented in the output, even if a department has no employees.

## How It Works

1. **Data Entry**: The program prompts the user to enter employee information (name, department, and salary) until they type "done".
2. **Processing**: The `process_employee_data` function calculates:
   - The total salary expense for each department
   - The average salary for each department
3. **Output**: The results are displayed in a dictionary format, showing each department’s total and average salaries.

## Requirements

- **Python 3.x**: Make sure Python 3 is installed on your system. No additional libraries are required.

## How to Run

### 1. **Download and Extract the ZIP File**
   - Download the ZIP file containing the project code.
   - Extract the contents of the ZIP file to a folder on your computer.

### 2. **Install Python (if not already installed)**
   - Ensure **Python 3.x** is installed on your computer. You can download it from [here](https://www.python.org/downloads/).

### 3. **Open a Terminal or Command Prompt**
   - Open the terminal (Linux/Mac) or command prompt (Windows).

### 4. **Navigate to the Extracted Folder**
   - Use the `cd` command to navigate to the folder where you extracted the ZIP file. For example:
     ```bash
     cd path/to/extracted/folder
     ```

### 5. **Run the Program**
   - Once you are in the correct folder, run the Python script with the following command:
     ```bash
     python dataProcessingTask.py
     ```

7. **Enter Data**:
   - The program will prompt you to enter employee data. Follow these steps:
     - Enter the employee’s name, department, and monthly salary as prompted.
     - Type "done" when you have finished entering data.
   - Once completed, the program will display the total and average salary for each department.


