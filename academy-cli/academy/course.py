import csv

class Course:
    def __init__(self) :
        pass       
    
    def __read_courses(self):
        with open ('files/courses.csv', 'r') as data:
            courses =  csv.DictReader(data)
            course_data = []
            for row in courses:
                course_data.append(row)
            return course_data
    
    def get_all_courses(self):
        courses = self.__read_courses()
        row1 = next(iter(courses))
        print(list(row1.keys()))
        for data in courses:
            print(list(data.values()))
        





    





