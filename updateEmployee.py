'''This file has the function to update the information in the file'''

#Import the files and libraries
import pandas as pd
import Employee
import checkData

'''This function does the following:
    1. Displays the current file information
    2. Gets the user input for the value to change, the ID of the employee to change and the new value
    3. Update the value in the dataframe and write to the file'''
def updateEmployee():
    Employee.listEmployee()
    df = pd.read_csv('employee.csv', index_col="ID")

    #Collect the ID of the employee whose information needs to be modified
    indexNo = str(input("Enter the ID of the employee you wish to make changes to ->  "))

    list_col = ["First Name","Last Name","Date of Employment","Salary","Department"]
    for value, col in enumerate(list_col):
        print(f"{value} - {col}")

    #Collect the column whose values needs to be changed     
    while(True):
        col = int(input("\nEnter the column to change -> "))

        #Perform checks for the new information to be entered in the dataframe
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

    #Update the dataframe using the syntax: df.loc[row, column] = new_value
    df.loc[int(indexNo), list_col[col]] = update_val

    #Update and display the CSV file
    df.to_csv('employee.csv')
    
    print("\nThe updated file:\n")
    Employee.listEmployee()


    