from  academy import Academy
from  student import Student


class Main (Academy, Student):
    option = 0

    # def __init__(self):
    #     pass
    if __name__ == "__main__":
        menu_selection()

    def menu_selection(self):
        options = {1:"Courses List"
                , 2: "Student List"
                , 3:"Inquiry"}
        print("welcome To IT Academy \n\n Please select an option::")
        for key , value   in options.items():
            print('{} : {}'.format(key , value))
        try:
            selected_option = int(input())
        except ValueError:
            print("please select an valid option")
            selected_option = int(input())
        if option > 3:
            print("please select an valid option")
            selected_option = int(input())
        return selected_option
        
    



m = Main()

def execute_option(option):
        if option == 1:
            m.get_all_courses()
        elif option == 2:
            m.get_all_students()
        elif option == 3:
            m.student_inquiry()

option = int(m.menu_selection())
# except ValueError:
#     print("please select an valid option")
#     option = m.menu_selection()
# if option > 3:
#     print("please select an valid option")
#     option = m.menu_selection()
execute_option(option)

    
# if option == 1:
#     m.get_all_courses()
# elif option == 2:
#     m.get_all_students()
# elif option == 3:
#     m.student_inquiry()

try:
    next_step = int(input("Enter 2 to continue to main menu and 1 to exit::  "))
except ValueError:
    next_step = int(input("Enter 2 to continue to main menu and 1 to exit::  "))

if next_step == 1:
    option = m.menu_selection()
    execute_option(option)







    





