import re

#Exception handling functions
def checkID(df):
    while True:
        id = input("Enter the employee ID (between 100 and 999): ")
        if not id.isdigit():
            print("You did not enter a numerical value! Please try again.")
            continue

        if int(id) not in df.index:
            if int(id) in range(100,1000):
                break
            else: print("You entered a value out of bound!")
        else: print("This value already exists in the file! Please try again.")

    return id

def checkFirstName(df):
    while True:
        name = input("Enter the first name: ")
        if name.isalpha():
            if name not in df['First Name'].values:
                break
            else: print("Name already exists! Please try again.")
        else: print("Enter only alphabetic values!")
            
    return name

def checkLastName(df):
    while True:
        name = input("Enter the last name: ")
        if name.isalpha():
            if name not in df['Last Name'].values:
                break
            else: print("Name already exists! Please try again.")
        else: print("Enter only alphabetic values!")
            
    return name

def checkDate():
    while True:
        date = input("Enter the date (MM-DD-YYY): ")
        pattern = r'^(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[01])-(199\d|20[01234]\d)$'

        if re.match(pattern, date):
            return date
        else:
            print("Please reenter in the correct format!")
            continue

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
