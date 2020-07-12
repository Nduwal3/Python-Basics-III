import csv

class Course:
    def __init__(self) :
        pass
        # self.id = id       
    
    def get_all_courses(self):
        with open ('files/courses.csv', 'r') as data:
            courses =  csv.reader(data)
            for rows in courses:
                print("{} : {}".format(rows[0], rows[1]))



# academy_obj.get_all_courses()



    





