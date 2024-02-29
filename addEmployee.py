'''This file contains the function to add a new row to the employee file'''

#Import files and libraries
import pandas as pd 
import Employee 
import checkData

'''The below function does the following:
    1. Call the functions defined in CheckData.py file for each value
    2. Using the contructor in the Employee class, initialize the values
    3. Call the to_dict() to get a dictionary of the values'''
def getEmployees(df):
    id = checkData.checkID(df)
    fname = checkData.checkFirstName(df)
    lname = checkData.checkLastName(df)
    date = checkData.checkDate()
    salary = checkData.checkSalary()
    dept = checkData.checkDepartment()

    emp = Employee.Employee(fname, lname, id, date, salary, dept)
    return emp.to_dict()
    

'''This function does the following:
    1. Read the CSv file to a dataframe
    2. Call the getEmployees() function to get the new row of values
    3. Convert the dictionary to a dataframe
    4. Append the new dataframe to the existing file using the append mode'''
def addEmployee():
    df = pd.read_csv('employee.csv', index_col="ID")
    data = getEmployees(df)
    newDF = pd.DataFrame([data])
    newDF.to_csv('employee.csv', mode= 'a', index= False, header=False)

    Employee.listEmployee()
