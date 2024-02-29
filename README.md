Employee Management System using Python
This Python project implements an Employee Management System utilizing the ‘pandas’ library to perform insertion, updating, and deletion operations on records stored in a CSV file. The project structure revolves around a menu-based interface where users can choose from various options to manage employee records.
Getting Started
To begin using the Employee Management System, follow these steps:
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Update the `employee.csv` file with your employee records in the specified format:
   ```
   ID, First name, Last name, Date of employment, Salary, Department
   ```
4. Run the `main.py` program to start the application.
Menu Structure
The menu structure of the Employee Management System is as follows:
1. **List**: View the list of all employee records.
2. **Add**: Add a new employee record to the system.
3. **Update**: Update an existing employee record.
4. **Remove**: Remove an employee record from the system.
5. **Exit**: Quit the program.
Key Concepts

The project incorporates several fundamental concepts of Python programming, including:
- Classes and objects for organizing code and data.
- Utilization of the pandas library to read, write, and manipulate CSV files efficiently.
- Working with DataFrames to represent and manage tabular data effectively.
Usage
Upon running `main.py`, users are presented with the menu options. They can select an option by entering the corresponding number. Depending on the selection, the program executes the associated function defined in the provided files.
Customization
If you wish to use your own CSV file, ensure it follows the specified format (`ID, First name, Last name, Date of employment, Salary, Department`). Replace the `employee.csv` file with your customized CSV file before running the program.
