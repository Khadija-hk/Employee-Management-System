'''This file contains the Employee class that defines the data 
    that is to be stored in the dataframe'''

#Import library
import pandas as pd 

'''The class Employee has the following declaration and definitions:
    1. Variable initializations in the constructor
    2. Function to collect the values and store it in a dictionary'''
class Employee:
    def __init__(self, fname, lname, empid, date_emp, salary, department):
        self.fname = fname
        self.lname = lname
        self.empid = empid
        self.date_emp = date_emp
        self.salary = salary
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
   
