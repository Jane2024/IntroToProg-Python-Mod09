# ------------------------------------------------------------------------ #
# Title: Assignment 09 "Main.py"
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# MBruce,9.7.2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    import DataClasses as D  # data classes
    from DataClasses import Employee as Emp  # Employee class only!
    import ProcessingClasses as P  # processing classes
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Define variables  --------------------------------------------------------#
strFileName = "EmployeeData.txt"
lst_of_file_data =[]
lst_of_emp =[]



# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
try:                                                                        # Try /except block to catch any file errors
    lst_of_file_data = Fp.read_data_from_file(strFileName)                  # Load data from file into list of objects
    lst_of_emp.clear()
    for item in lst_of_file_data:                                           # breakout each data item from emp object and store in lst of emp
        lst_of_emp.append(Emp(item[0], item[1], item[2].strip()))

    while (True):                                                           # Loop to allow user to choose options till exiting
        # Show user a menu of options
        Eio.print_menu_items()                                              # Display the menu

        # Get user's menu option choice
        choice_str= (Eio.input_menu_options())                              # Get the users menu choice

        # Show user current data in the list of employee objects
        if choice_str.strip() == '1':
            Eio.print_current_list_items(lst_of_emp)                        # Based on user choice "1", display current list of employees
            continue


        # Let user add data to the list of employee objects
        elif choice_str.strip() == '2':
            emp = Eio.input_employee_data()                                 # Based on user choice "2", add employee and then add to list of employees
            lst_of_emp.append(emp)
            continue  # to show the menu


        # let user save current data to file
        elif choice_str == '3':
            if Fp.save_data_to_file(strFileName, lst_of_emp) == True:       # Based on user choice "3", save data to file and check for success
                print("Data Saved!")

            else:
                print("something went wrong. Data was not saved to file.")  # If file save failed, notify user.

            continue  # to show the menu

        # Let user exit program
        elif choice_str == '4':                                              # Based on user choice "4", exit program
            print("Goodbye!")
            break  # by exiting loop


except Exception as e:                                                       # If file error, catch it and notify user.
    print("Dude, you got an file error!")
    print(e,e.__doc__,sep="\n")

# Main Body of Script  ---------------------------------------------------- #
