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


def show_course_student(courses_list,course_student):
        if len(courses_list) == 0:
            print("please input courses information")
        else:
            show_courses(courses_list)   
            choose = int(input("Choose course: "))
            if choose > len(courses_list) or choose < 1:
                print('Invalid course')
            else:
                if len(course_student[choose-1]) == 0:
                    print("No student in the course")
                else:
                    print('Student in course:')
                    for i in range (len(course_student[choose-1])):
                        print(f"| ID: {course_student[choose-1][i].getId()} | FULL NAME: {course_student[choose-1][i].getName()} | DATE OF BIRTH: {course_student[choose-1][i].getDob()} |")


def show_mark(course_list,student_list,course_student):
        if len(student_list) == 0 or len(course_list) == 0:
            print("Please input information for students and courses")
        else:
            show_courses(course_list)
            choose = int(input("Choose course: "))
            if choose < 1 or choose > len(course_list):
                print("Invalid choice!")
            else:
                if len(course_student[choose-1]) != 0:
                    for i in range(len(course_student[choose-1])):
                        if course_student[choose-1][i].mark[f"Mark_{course_list[choose-1].getName()}"] != None:
                            print(f"""| ID: {course_student[choose-1][i].getId()} | FULL NAME: {course_student[choose-1][i].getName()} | DATE OF BIRTH: {course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: {course_student[choose -1][i].mark[f"Mark_{course_list[choose-1].getName()}"]} | """)
                        else:
                             print(f"""| ID: {course_student[choose-1][i].getId()} | FULL NAME: {course_student[choose-1][i].getName()} | DATE OF BIRTH: {course_student[choose-1][i].getDob()} | Mark_{course_list[choose-1].getName()}: No input | """)                         
                else:
                    print("The course is empty")


def show_gpa(student_list,course_list):
        if len(student_list) == 0 or len(course_list) == 0:
            print("Please input information for students and courses")
        else:
            show_students(student_list)
            student_id = input("Student ID: ")
            exist = False
            for student in student_list:
                if student_id == student.getId():
                    print(f"| ID: {student.getId()} | FULL NAME: {student.getName()} | DATE OF BIRTH: {student.getDob()} | GPA: {student.gpa_cal()} | Including: {student.course_joining()} |")
                    exist = True
            if exist == False:
                print("The id does not exist")
            
def sorting_gpa(student_list,course_list):
        if len(student_list) == 0 or len(course_list) == 0:
            print("Please input information for students and courses")
        else:
            student_sort= sorted(student_list, key=lambda student: student.gpa_cal(), reverse = True)
            for i in student_sort:
                print(f"| ID: {i.getId()} | FULL NAME: {i.getName()} | DoB: {i.getDob()} | GPA: {i.gpa_cal()} | INCLUDING: {i.course_joining()}")
