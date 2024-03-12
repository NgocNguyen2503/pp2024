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


    def show_students(self,students_list):
        print("------------------------------------")
        if len(students_list) == 0:     # if the list is empty
            print("The student list is empty")
        else:
            print("Student list:")
            for i in range(len(students_list)):
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
        self.show_students(students_list)
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
            choose = int(input("Choose course to input: "))
            if choose > len(course_list) or choose < 1:
                print("Invalid choice!")
            else:
                if len(self.course_student[choose-1]) == 0:
                    print("No student in the course")
                else:
                    print('Student in course:')
                    for i in range (len(self.course_student[choose-1])):
                        if self.course_student[choose-1][i].mark[f"Mark_{course_list[choose-1].getName()}"] != None:
                            print(f"""| ID: {self.course_student[choose-1][i].getId()} | FULL NAME: {self.course_student[choose-1][i].getName()} | DATE OF BIRTH: {self.course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: {self.course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"]} """)
                        else:
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
                        if self.course_student[choose-1][i].mark[f"Mark_{course_list[choose-1].getName()}"] != None:
                            print(f"""| ID: {self.course_student[choose-1][i].getId()} | FULL NAME: {self.course_student[choose-1][i].getName()} | DATE OF BIRTH: {self.course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: {self.course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"]} | """)
                        else:
                             print(f"""| ID: {self.course_student[choose-1][i].getId()} | FULL NAME: {self.course_student[choose-1][i].getName()} | DATE OF BIRTH: {self.course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: No input | """)                         
                else:
                    print("The course is empty")


def main():
    u = University()
    while True:
        print("\n________________OPTIONS_________________")
        print("0. Close the program")
        print("1. Input student information (ID, name, DoB)")
        print("2. Input courses information (ID, course name)")
        print("3. Assign students to courses")
        print("4. input student mark in course")
        print("5. print student list")
        print("6. print course list")
        print("7. print list student in each course")
        print("8. print students mark in each course")
              
        choose = input("Option: ")
        if choose == '0':
            break

        elif choose == '1':
            print("\n---------------------------")
            number_student = u.number_student()
            print("---------------------------")
            print("\n---------------------------")
            print("Input students information:")
            if number_student == None:
                print("Please input number of student")
            else:
                for _ in range (number_student):
                    print(f"Student {_+1}:")
                    u.student_list.append(u.input_student())
                    print("\n")
            print("---------------------------")

        elif choose == '2':
            print("\n---------------------------")
            number_course = u.number_course()
            print("---------------------------")
            u.course_student = [[] for _ in range(number_course)]
            print("\n---------------------------")
            print("Input course information: ")
            if number_course == None:
                print("Please input number of course")
            else:
                for _ in range (number_course):
                    print(f"Course {_+1}:")
                    u.course_list.append(u.input_course())
                    print("\n")
            print("---------------------------")

        elif choose == '3':
            print("\n---------------------------")
            print("Assign student into courses")
            u.choose_course(u.course_list, u.student_list)
            print("---------------------------")

        elif choose == '4':
            print("\n---------------------------")
            print("Input mark in each course")
            u.input_mark(u.course_list)
            print("---------------------------")

        elif choose == '5':
            print("\n---------------------------")
            print("Print student list")
            u.show_students(u.student_list)
            print("---------------------------")

        elif choose == '6':
            print("\n---------------------------")
            print("Print course list")
            u.show_courses(u.course_list)
            print("---------------------------")

        elif choose == '7':
            print("\n---------------------------")
            print("Print students in each course")
            print("---------------------------")
            u.show_course_student(u.course_list,)
            print("---------------------------")

        elif choose == '8':
            print("\n---------------------------")
            print("Print students mark in each course")
            print("---------------------------")
            u.show_mark(u.course_list,u.student_list)
            print("---------------------------")

        else:
            print("\n---------------------------")
            print("Not valid option\nPlease input again")
            print("---------------------------")




if __name__ == "__main__":
    main()







    
    
    




