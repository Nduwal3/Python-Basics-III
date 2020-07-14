import csv


class Student:    
    def __init__(self):
        # this.mode = mode
        # this.data = data
        pass

    def file_read_write(self, mode, data=None):
        with open ('files/students.csv', mode) as student_data:
            
            result=[]
            if mode == 'r':
                students =  csv.DictReader(student_data)
                if students is not None:
                    for row in students:
                        result.append(row)
            else:
                # Create a writer object from csv module
                students =  csv.writer(student_data)
                # Add contents of list as last row in the csv file
                students.writerow(data)
        return result


    def get_all_students(self, mode):
        students_list = self.file_read_write(mode)
        val = next(iter(students_list))
        print(list(val.keys()))
        for item in students_list:
            print(list(item.values()))

    def get_Student_info(self, name, mode):
        students_list = self.file_read_write(mode)
        for item in students_list:
            if name in item.values():
                print(item)
            else:
                print("no record found")
                break

    def update_student_detail(self, id, mode):
        students_list = self.file_read_write(mode)
        print("update_student_detail")
        print(mode)

    def create_new_student(self, student_data, mode):
        print(student_data)
        students_list = self.file_read_write(mode, data = student_data)
        print(self.__get_records_count(students_list))
        
        print("update_student_detail")
        print(mode)
        
        pass

    def delete_student(self, name, mode):
        updated_list =[]
        students_list = self.file_read_write(mode)
        for student in students_list:
            if student.get('student_name') != name:
                updated_list.append(student)
        self.__update_file(updated_list)
    
    def __update_file(self, updatedlist):
        print(updatedlist)
        val = next(iter(updatedlist))
        header = list(val.keys())
        print(header)
        with open('files/students.csv',"w") as f:
            Writer=csv.DictWriter(f, fieldnames=header)
            Writer.writeheader()
            for row in updatedlist:
                Writer.writerow(row)
            print("File has been updated")

    def __get_records_count(self, student_list):
        return student_list[-1:]

    