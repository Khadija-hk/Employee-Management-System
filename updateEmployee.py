import pandas as pd
import Employee
import checkData

#Write a function to update the employees based on the Index (ID)
def updateEmployee():
    Employee.listEmployee()
    df = pd.read_csv('employee.csv', index_col="ID")

    indexNo = str(input("Enter the ID of the employee you wish to make changes to ->  "))
    list_col = ["First Name","Last Name","Date of Employment","Salary","Department"]
    for value, col in enumerate(list_col):
        print(f"{value} - {col}")
    
    while(True):
        col = int(input("\nEnter the column to change -> "))

        if col == 0:
            update_val = checkData.checkFirstName(df)
            break
        elif col == 1:
            update_val = checkData.checkLastName(df)
            break
        elif col == 2:
            update_val = checkData.checkDate()
            break
        elif col == 3:
            update_val = checkData.checkSalary()
            break
        elif col == 4:
            update_val = checkData.checkDepartment()
            break
        else: print("\nEnter a valid column!")

    df.loc[int(indexNo), list_col[col]] = update_val

    df.to_csv('employee.csv')
    
    print("\nThe updated file:\n")
    Employee.listEmployee()


    