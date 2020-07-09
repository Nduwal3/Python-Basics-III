class Main (Academy, Student):
    pass

    # def __init__(self):
    #     pass

    def menu_selection(self):
        options = {1:"Courses List"
                , 2: "Student List"
                , 3:"Inquiry"}
        print("welcome To IT Academy \n Please select an option::\n")
        for key , value   in options.items():
            print('{} : {}'.format(key , value))
        selected_option = int(input())
        return selected_option
        
    def execute_option(self, option):
        if option == 1:
            get_all_courses(self)
        elif option == 2:
            get_all_students()
        elif option == 3:
            student_inquiry()



m = Main()
option = m.menu_selection()
m.execute_option(option)




