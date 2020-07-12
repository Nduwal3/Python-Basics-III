import csv


class Student:

    
    def __init__(self, mode):
        this.mode = mode
        # this.data = data
        pass

    def file_read_write(self, mode, data=None, id=None):
        # if mode = 'r':
        # else: mode = 'a'
        with open ('files/students.csv', mode) as data:
            students =  csv.reader(data)
            if data is not None:
                print(data)
                # students.write(data)
            if id is not None:
                print(id)


    def get_all_students(self):
        
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

    