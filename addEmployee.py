#Add exception handling
import pandas as pd 
import Employee 
import checkData


#Get the employee details to add    
def getEmployees(df):
    id = checkData.checkID(df)
    fname = checkData.checkFirstName(df)
    lname = checkData.checkLastName(df)
    date = checkData.checkDate()
    salary = checkData.checkSalary()
    dept = checkData.checkDepartment()

    emp = Employee.Employee(fname, lname, id, date, salary, dept)
    return emp.to_dict()
    


#Add the employees to the file
def addEmployee():
    df = pd.read_csv('employee.csv', index_col="ID")
    data = getEmployees(df)
    newDF = pd.DataFrame([data])
    newDF.to_csv('employee.csv', mode= 'a', index= False, header=False)

    Employee.listEmployee()
