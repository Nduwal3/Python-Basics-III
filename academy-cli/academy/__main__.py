import sys
from .course import Course
from .student import Student

def main():
    print("welcomme to IT Academy")
    studentObj = Student()
    courseObj = Course()
    choice = ''
    sub_choice = ''


    while choice != 'q': 
        choice = get_user_choice()

        # Respond to the user's choice.
        if choice == '1':
            sub_choice = get_student_options()
        elif choice == '2':
            sub_choice = get_course_options()
        elif choice == 'q':
            print("\n Bye Bye.")
        else:
            print("\nI didn't understand that choice.\n")


        if choice == '1' and sub_choice =='1':            
            studentObj.get_all_students(mode='r')
        elif choice == '1' and sub_choice =='2':
            name = input("enter your fullname:::eg(John Doe)\n")
            studentObj.get_Student_info(format_name(name), mode='r')
        elif choice == '1' and sub_choice =='3':
            name = input("enter your fullname:::eg(John Doe)\n")
            studentObj.update_student_detail(format_name(name), mode='a'), 
        elif choice == '1' and sub_choice =='4':
            student_data = student_create_data()
            studentObj.create_new_student(student_data, mode='a+')
        elif choice == '1' and sub_choice =='5':
            name = input("enter your fullname:::eg(John Doe)\n")
            studentObj.delete_student(format_name(name), mode='r')
        elif choice =='2' and sub_choice == '1':
            courseObj.get_all_courses()

        elif choice == 'q':
            print("\n Bye Bye.")
        else:
            print("\nI didn't understand that choice.\n")

    # args = sys.argv[1:]
    # print('count of args::{}'.format(len(args)))
    
    # for arg in args:
    #     print('passed argument::{}'.format(arg))    

def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Enter into Student Module.")
    print("[2] Enter Course Module.")
    print("[q] Quit.")
    return input("What would you like to do? ")

def get_student_options():
    print("\n[1] get all Students information")
    print("[2] view your Students profile")
    print("[3] Update your profile.")
    print("[4] Register into course")
    print("[5] Delete your Courses.")
    print("[q] Quit.")
    return input("What would you like to do? ")

def get_course_options():
    print("\n[1] Enquire about Course")
    # print("[2] Enroll into a course.")
    print("[q] Quit.")    
    return input("What would you like to do? ")

def student_create_data():
    name = input("enter your fullname:::eg(John Doe)\n")
    email = input("enter your email:::eg(John@mail.com)\n")
    course = input("enter Courses to enroll:::eg(python)\n")
    balance = input("make full installment :::eg(1000000)\n")
    data = []
    data.append(format_name(name))
    data.append(email)
    data.append(balance)
    return data


def format_name(name):
    fullname = name.split(' ')
    for i in range(len(fullname)):
        fullname[i] = fullname[i].capitalize()
    formatted_string =  ' '.join(fullname)
    return formatted_string
    

if __name__ == '__main__':
    main()