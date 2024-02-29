'''This file contains the function that helps remove the employee from the file'''

#Import the libraries and files
import pandas as pd
import Employee

'''This function takes in the index of the row to be deleted, once the 
    index is validated, it uses the 'drop' function to delete it from the file'''
def removeEmployee():
    Employee.listEmployee()
    df = pd.read_csv('employee.csv', index_col="ID")

    #Validate the ID that the user wants to delete
    while True:
        value = int(input("\nEnter the Employee ID you wish to remove: "))
        if int(value) not in df.index:
            print("\nEnter a valid index!")
        else:   break

    #Deleting the value using the 'drop' function
    df = df.drop(index=[value])
    
    df.to_csv('employee.csv')
    
    print("\nThe updated file:\n")
    Employee.listEmployee()
