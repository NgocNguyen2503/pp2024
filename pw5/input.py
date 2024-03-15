from domain.student import Student
from domain.course import Course
from output import show_courses, show_students
import math
import zlib

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


def write_students(student_list):
    with open("students.txt", "w") as f:
        for i,student in enumerate(student_list):
            if i == (len(student_list)-1):
                f.write(f"{student.getId()},{student.getName()},{student.getDob()}")
            else:
                f.write(f"{student.getId()},{student.getName()},{student.getDob()}\n")
        f.write("!")
    f.close()

def write_courses(course_list):
    with open("courses.txt", "w") as f:
        for i,course in enumerate(course_list):
            if i == (len(course_list)-1):
                f.write(f"{course.getId()},{course.getName()}")
            else:
                f.write(f"{course.getId()},{course.getName()}\n")
        f.write("!")
    f.close()
'''
def write_mark(student_list):
    f = open("marks.txt","w")
    for i,student in enumerate(student_list):
        if i == (len(student_list)-1):
            f.write(f"|{student.getId()}|{student.getName()}")
            for course, mark in student.mark.items():
                f.write(f"|{course}|{mark}")
        else:
            f.write(f"|{student.getId()}|{student.getName()}")
            for course, mark in student.mark.items():
                f.write(f"|{course}|{mark}"+"\n")
    f.close()
'''
def write_mark(student_list):
    with open("marks.txt", "w") as f:
        for i, student in enumerate(student_list):
            f.write(f"{student.getId()},{student.getName()}")
            for course, mark in student.mark.items():
                f.write(f",{course},{mark}")
            if i < len(student_list) - 1:
                f.write("\n")

def compress_files():
        with open("students.txt", "rb") as f:
            students_data = f.read()
        with open("courses.txt", "rb") as f:
            courses_data = f.read()
        with open("marks.txt", "rb") as f:
            marks_data = f.read()

        compressed_data = zlib.compress(students_data + courses_data + marks_data)

        with open("students.dat", "wb") as f:
            f.write(compressed_data)

def decompress_files(student_list,course_list,course_student):

    with open("students.dat", "rb") as f:
        compressed_data = f.read()

    decompressed_data = zlib.decompress(compressed_data)

    convert_data = decompressed_data.decode()  # Convert from bytes to string
    x=convert_data.split("!")
    students,courses,marks = x
    with open("students.txt", "w") as f:
        f.write(students)
        lines = students.split("\n")
        for i in lines:
           data = i.split(",")
           st_id,name,dob = data
           student_list.append(Student(st_id,name,dob))
        
    with open("courses.txt", "w") as f:
        f.write(courses)
        lines = courses.split("\n")
        for i in lines:
           data = i.split(",")
           cs_id,name = data
           course_list.append(Course(cs_id,name))

    with open("marks.txt", "w") as f:
        f.write(marks)
        lines = marks.split("\n")
        for i in lines:
            data = i.split(",")
            st_id, name, *mark_list = data
            print(f"a + {mark_list}")
            for student in student_list:
                if st_id == student.getId():
                    for j in range(0, len(mark_list), 2):
                        course = mark_list[j]
                        mark = mark_list[j + 1]
                        student.mark[course] = mark
                    





    



                
                

