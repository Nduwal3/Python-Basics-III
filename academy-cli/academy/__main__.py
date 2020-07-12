import sys
from .course import Course
from .student import Student

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args::{}'.format(len(args)))
    print("welcomme to IT Academy")
    options = {1:"inquiry"
                , 2: "Enroll"
                , 3:"Update"
                , 4: "Delete"}
    optionII= {1:"student",2:"course"}
    for arg in args:
        print('passed argument::{}'.format(arg))
    studentObj = Student()
    courseObj = Course()
    

if __name__ == '__main__':
    main()