import csv


class Student:

    def __init__(self):
        pass

    def get_all_students(self):
        with open ('files/students.csv', 'r') as data:
            students =  csv.reader(data)
            print("The list of students are::\nS")
            for rows in students:
                print("{} : {}".format(rows[0], rows[1]))
            print("\n")

    def get_Student_info(self, id):
        pass

    def update_student_detail(self, id):
        pass

    def delete_student(self, id):
        pass

    