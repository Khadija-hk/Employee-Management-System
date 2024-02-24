import re
import exception

#Exception handling functions
def checkID(df):
    while True:
        try:
            id = input("Enter the employee ID (between 100 and 999): ")

            if int(id) not in df.index:
                if int(id) in range(100,1000):
                    return id
                else: print("You entered a value out of bound!")
            else: print("This value already exists in the file! Please try again.")
        except ValueError:
            print("You did not enter a numerical value! Please try again.")


def checkFirstName(df):
    while True:
        try:
            name = input("Enter the first name: ")
            if not name.isalpha():
                raise exception.NonAlphabeticNameErrror()
            if name not in df['First Name'].values:
                return name
            else: print("Name already exists! Please try again.")
        except exception.NonAlphabeticNameErrror as e:
            print(e)
            
    

def checkLastName(df):
    while True:
        try:
            name = input("Enter the last name: ")
            if not name.isalpha():
                raise exception.NonAlphabeticNameErrror()
            if name not in df['Last Name'].values:
                return name
            else: print("Name already exists! Please try again.")
        except exception.NonAlphabeticNameErrror as e:
            print(e)
            

def checkDate():
    while True:
        try:
            date = input("Enter the date (MM-DD-YYY): ")
            pattern = r'^(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[01])-(199\d|20[01234]\d)$'

            if re.match(pattern, date):
                return date
            else:
                raise exception.InvalidDateFormat()
        except exception.InvalidDateFormat as e:
            print(e)

def checkSalary():
    while True:
        salary = input("Enter the salary: ")
        if int(salary) in range(10000,100001):
            return salary
        else:
            print("Please check the amount you entered! (Between 10,000 and 100,000)")
            continue

def checkDepartment():
    departmentList = ['it','accounting','finance','designs','marketing','sales']
    print("Choose the department from the following: ")
    for value, department in enumerate(departmentList):
        print(f"{value} - {department}")
    
    while True:
        dept = int(input("Enter your choice: "))
        if dept in range(0,len(departmentList)):
            return departmentList[dept]
        else:
            print("Wrong choice! Please try again.")
