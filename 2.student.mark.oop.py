class Student:
    def __init__(self,id,name,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.mark = {}

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__dob
    
        
class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name

class University:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.course_student = []

    def number_student(self):
        self.st_number = int(input("Number of student: "))
        return self.st_number
    
    def number_course(self):
        self.cs_number = int(input("Number of course: "))
        return self.cs_number
    
    def input_student(self):
        id = input("Student ID: ")
        name= input("Full name: ")
        DoB = input("Date of birth: ")
        return Student(id,name,DoB)

    def input_course(self):
        id = input("Course ID: ")
        name = input("Name: ")
        return Course(id,name)
    
    def show_students(self,students_list, number_student):
        print("------------------------------------")
        if len(students_list) == 0:     # if the list is empty
            print("The student list is empty")
        else:
            print("Student list:")
            for i in range(number_student):
                print(f"{i + 1} | ID: {students_list[i].getId()} | FULL NAME: {students_list[i].getName()} | DATE OF BIRTH: {students_list[i].getDob()} |")
        print("------------------------------------")


    def show_courses(self,courses_list):
        print("------------------------------------")
        if len(courses_list) == 0:      # if the list is empty
            print("The course list is empty")
        else:
            print("Course list: ")
            for i in range(len(courses_list)):
                print(f"{i + 1} | COURSE ID: {courses_list[i].getId()} | COURSE NAME: {courses_list[i].getName()}")
        print("------------------------------------")

    def assign_students(self,students_list):
        print("input assigned student: ")
        assigned_st = []
        student_in_course = []
        while True:
            st_id = input("ID (type enter to stop input): ")
            if st_id == '':
                print("STOP INPUT")
                break
            assigned_st.append(st_id)
        for i in range(len(assigned_st)):
            success = False
            for j in range(len(students_list)):
                if assigned_st[i] == students_list[j].getId():
                    student_in_course.append(students_list[j])
                    success = True
                    print('Assigned successful')
            if(success == False):
                print(f"The ID: {assigned_st[i]} does not exist ")
        return student_in_course


    def choose_course(self,courses_list, students_list):
        if len(courses_list) == 0 or len(students_list) == 0:
            print("Please input courses & students information")
        else:
            self.show_courses(courses_list)
            choose = int(input("Choose a course to assign student: "))
            if choose > len(courses_list) or choose < 1:
                print('Invalid course')
            else:
                self.course_student[choose-1].extend(self.assign_students(students_list))
                for i in range (len(self.course_student[choose-1])):
                    # Error part
                    self.course_student[choose-1][i].mark[f"Mark_{courses_list[choose-1].getName()}"] = None

    def show_course_student(self,courses_list):
        if len(courses_list) == 0:
            print("please input courses information")
        else:
            self.show_courses(courses_list)   
            choose = int(input("Choose course: "))
            if choose > len(courses_list) or choose < 1:
                print('Invalid course')
            else:
                if len(self.course_student[choose-1]) == 0:
                    print("No student in the course")
                else:
                    print('Student in course:')
                    for i in range (len(self.course_student[choose-1])):
                        print(f"| ID: {self.course_student[choose-1][i].getId()} | FULL NAME: {self.course_student[choose-1][i].getName()} | DATE OF BIRTH: {self.course_student[choose-1][i].getDob()} |")


    def input_mark(self,course_list):
        if len(course_list) == 0:
            print("Please input information for courses")
        else:
            self.show_courses(course_list)
            choose = int(input("Choose course to input"))
            if choose > len(course_list) or choose < 1:
                print("Invalid choice!")
            else:
                if len(self.course_student[choose-1]) == 0:
                    print("No student in the course")
                else:
                    print('Student in course:')
                    for i in range (len(self.course_student[choose-1])):
                        print(f"| ID: {self.course_student[choose-1][i].getId()} | FULL NAME: {self.course_student[choose-1][i].getName()} | DATE OF BIRTH: {self.course_student[choose-1][i].getDob()} |")
                    st_input = input("Student ID: ")
                    exist = False
                    for i in range(len(self.course_student[choose-1])):
                        if st_input == self.course_student[choose-1][i].getId():
                            exist = True
                            mark = float(input("Mark: "))
                            self.course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"] = mark
                    if exist == False:
                        print(f"The ID {st_input} does not exist")

    def show_mark(self,course_list,student_list):
        if len(student_list) == 0 or len(course_list) == 0:
            print("Please input information for students and courses")
        else:
            self.show_courses(course_list)
            choose = int(input("Choose course: "))
            if choose < 1 or choose > len(course_list):
                print("Invalid choice!")
            else:
                if len(self.course_student[choose-1]) != 0:
                    for i in range(len(self.course_student[choose-1])):
                        print(f"""| ID: {self.course_student[choose-1][i].getId()} | FULL NAME: {self.course_student[choose-1][i].getName()} | DATE OF BIRTH: {self.course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: {self.course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"]} """)
                else:
                    print("The course is empty")


def main():
    u = University()
    
    st_number = u.number_student()
    for _ in range(st_number):
        print(f"Student {_+1}: ")
        u.student_list.append(u.input_student())
        
    u.show_students(u.student_list,st_number)
       
    cs_number = u.number_course()
    u.course_student = [[] for _ in range(cs_number)]
    for _ in range(cs_number):
        print(f"Course {_+1}: ")
        u.course_list.append(u.input_course())
    
    u.show_courses(u.course_list)
    u.choose_course(u.course_list,u.student_list)
    u.show_course_student(u.course_list)
    u.input_mark(u.course_list)
    u.show_mark(u.course_list, u.student_list)
 

if __name__ == "__main__":
    main()




    
    
    




