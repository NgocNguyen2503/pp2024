from domain.student import Student
from domain.course import Course
from output import show_courses, show_students
import math
import gzip

def number_students():
    st_number = int(input("Number of student: "))
    return st_number


def number_courses():
    cs_number = int(input("Number of course: "))
    return cs_number


def input_student():
    id = input("Student ID: ")
    name= input("Full name: ")
    DoB = input("Date of birth: ")
    return Student(id,name,DoB)


def input_course():
    id = input("Course ID: ")
    name = input("Name: ")
    return Course(id,name)

'''
def show_students(students_list):
    print("------------------------------------")
    if len(students_list) == 0:     # if the list is empty
        print("The student list is empty")
    else:
        print("Student list:")
        for i in range(len(students_list)):
            print(f"| ID: {students_list[i].getId()} | FULL NAME: {students_list[i].getName()} | DATE OF BIRTH: {students_list[i].getDob()} |")
    print("------------------------------------")


def show_courses(courses_list):
    print("------------------------------------")
    if len(courses_list) == 0:      # if the list is empty
        print("The course list is empty")
    else:
        print("Course list: ")
        for i in range(len(courses_list)):
            print(f"INDEX: {i + 1} | COURSE ID: {courses_list[i].getId()} | COURSE NAME: {courses_list[i].getName()}")
    print("------------------------------------")
'''

def assign_students(students_list):
    print("input assigned student: ")
    assigned_st = []
    student_in_course = []
    show_students(students_list)
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


def choose_course(courses_list, students_list, course_student):
    if len(courses_list) == 0 or len(students_list) == 0:
        print("Please input courses & students information")
    else:
        show_courses(courses_list)
        choose = int(input("Choose a course to assign student: "))
        if choose > len(courses_list) or choose < 1:
            print('Invalid course')
        else:
            course_student[choose-1].extend(assign_students(students_list))
            for i in range (len(course_student[choose-1])):
                course_student[choose-1][i].mark[f"Mark_{courses_list[choose-1].getName()}"] = None

def input_mark(course_list,course_student):
        if len(course_list) == 0:
            print("Please input information for courses")
        else:
            show_courses(course_list)
            choose = int(input("Choose course to input: "))
            if choose > len(course_list) or choose < 1:
                print("Invalid choice!")
            else:
                if len(course_student[choose-1]) == 0:
                    print("No student in the course")
                else:
                    print('Student in course:')
                    for i in range (len(course_student[choose-1])):
                        if course_student[choose-1][i].mark[f"Mark_{course_list[choose-1].getName()}"] != None:
                            print(f"""| ID: {course_student[choose-1][i].getId()} | FULL NAME: {course_student[choose-1][i].getName()} | DATE OF BIRTH: {course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: {course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"]} """)
                        else:
                            print(f"| ID: {course_student[choose-1][i].getId()} | FULL NAME: {course_student[choose-1][i].getName()} | DATE OF BIRTH: {course_student[choose-1][i].getDob()} |")
                    st_input = input("Student ID: ")
                    exist = False
                    for i in range(len(course_student[choose-1])):
                        if st_input == course_student[choose-1][i].getId():
                            exist = True
                            mark = float(input("Mark: "))
                            course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"] = math.floor(mark*10)/10
                    if exist == False:
                        print(f"The ID {st_input} does not exist")


def write_student(student_list):
    f = open("Student.txt","w")
    for i in student_list:
        f.write(f"| ID: {i.getId()} | FULL NAME: {i.getName()} | DoB: {i.getDob()}" + "\n")
    f.close()

def write_course(course_list):
    f = open("Course.txt","w")
    for i in course_list:
        f.write(f"| ID: {i.getId()} | NAME: {i.getName()} |" + "\n")
    f.close()

def write_mark(student_list):
    f = open("Mark.txt","w")
    for i in student_list:
        f.write(f"| ID: {i.getId()} | FULL NAME: {i.getName()}")
        for course, mark in i.mark.items():
            f.write(f" | Course: {course} | Mark: {mark} |\n")
    f.close()

def compress_infor():
    with gzip.open("Student.zip","wb") as f:
        student = open("Student.txt","rb")
        f.write(student.read())
        course = open("Course.txt","rb")
        f.write(course.read())
        mark = open("Mark.txt","rb")
        f.write(mark.read())


def decompress_infor():
    try:
        with gzip.open("Student.zip","rb") as f:
            student = open("Student.txt","wb")
            student.write(f.read())
            course = open("Course.txt","wb")
            course.write(f.read())
            mark = open("Mark.txt","wb")
            mark.write(f.read())
    except FileNotFoundError:
        print("compressed file does not exist")

                
                

