# Add the file name input - user should enter the file name
# add checking for the continue function
import Employee
import addEmployee
import removeEmployee
import updateEmployee

def continueProgram():
    ans = input("\n Do you wish to continue? (Y/N): ")
    if ans.lower() == 'y': return True
    else: return False

def menu():
    while True:
        print("\n Welcome to Employee Management System!")
        print("Menu: ")
        print("1. List Employees. ")
        print("2. Add Employees. ")
        print("3. Update Employees. ")
        print("4. Remove Employees. ")
        print("5. Exit! ")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            #List employee function 
            Employee.listEmployee()

            if continueProgram() != True: break
            
        elif choice == 2:
            #Add employee function
            addEmployee.addEmployee()

            if continueProgram() != True: break

        elif choice == 3:
            #Update employee            
            updateEmployee.updateEmployee()

            if continueProgram() != True: break
        
        elif choice == 4:
            #Remove employee
            removeEmployee.removeEmployee()
            
            if continueProgram() != True: break

        elif choice == 5:
            #Exit program
            print("\n Thank you for using the Employee Management system!")
            break
        
        else:
            print("\n Wrong choice! Enter again")



if __name__ == "__main__":
    menu()