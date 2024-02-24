import pandas as pd
import Employee

def removeEmployee():
    Employee.listEmployee()
    df = pd.read_csv('employee.csv', index_col="ID")
    while True:
        value = int(input("\nEnter the Employee ID you wish to remove: "))
        if int(value) not in df.index:
            print("\nEnter a valid index!")
        else:   break

    df = df.drop(index=[value])
    
    df.to_csv('employee.csv')
    
    print("\nThe updated file:\n")
    Employee.listEmployee()
