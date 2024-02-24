import pandas as pd 

class Employee:
    def __init__(self, fname, lname, empid, date_emp, salary, department):
        self.fname = fname
        self.lname = lname
        self.empid = empid
        self.date_emp = date_emp
        self.salary = salary
        self.department = department 
    
    #Using getters and setters
    def get_fname(self):
        return self.fname
    def set_fname(self, name):
        self.fname = name

    def get_lname(self):
        return self.lname
    def set_lname(self, name):
        self.lname = name
    
    def get_empid(self):
        return self.empid
    def set_empid(self, id):
        self.empid = id
    
    def get_date_emp(self):
        return self.date_emp
    def set_date_emp(self, date):
        self.date_emp = date

    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary

    def get_department(self):
        return self.department
    def set_department(self, department):
        self.department = department

    def to_dict(self):
        return{
            "ID" : self.empid,
            "First Name": self.fname,
            "Last Name" : self.lname,
            "Date of Employment" : self.date_emp,
            "Salary" : self.salary,
            "Department" : self.department
        }

#Import the file and display the contents
def listEmployee():
    df = pd.read_csv('employee.csv', index_col="ID")
    print(df)
   







