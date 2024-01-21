def number_students():
    st_number = int(input("Number of student: "))
    return st_number


def number_courses():
    cr_number = int(input("Number of courses: "))
    return cr_number


def input_students():
    st_infor = {}    #Create dictionary for information set
    st_infor["Student ID"] = input("Student ID: ")
    st_infor["Full name"] = input("Full name: ")
    st_infor["DoB"] = input("Date of birth (day/month/year): ")
    return st_infor


def input_course():
    cr_infor = {} # Create dictionary for information set
    cr_infor['Course ID'] = input("Course ID: ")
    cr_infor['Course name'] = input('Course name: ')
    return cr_infor


def show_students(students_list, number_student):
    print("------------------------------------")
    if len(students_list) == 0:     # if the list is empty
        print("The student list is empty")
    else:
        print("Student list:")
        for i in range(number_student):
            print(f"{i + 1} | ID: {students_list[i]['Student ID']} | FULL NAME: {students_list[i]['Full name']} | DATE OF BIRTH: {students_list[i]['DoB']} |")
    print("------------------------------------")


def show_courses(courses_list, number_course):
    print("------------------------------------")
    if len(courses_list) == 0:      # if the list is empty
        print("The course list is empty")
    else:
        print("Course list: ")
        for i in range(number_course):
            print(f"{i + 1} | COURSE ID: {courses_list[i]['Course ID']} | COURSE NAME: {courses_list[i]['Course name']}")
    print("------------------------------------")


def assign_students(students_list):
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
            if assigned_st[i] == students_list[j]['Student ID']:
                student_in_course.append(students_list[j])
                success = True
                print('Assigned successful')
        if(success == False):
            print(f"The ID: {assigned_st[i]} does not exist ")
    return student_in_course


def choose_course(courses_list,number_course, students_list, course_student):
    if len(courses_list) == 0 or len(students_list) == 0:
        print("Please input courses & students information")
    else:
        show_courses(courses_list, number_course)
        choose = int(input("Choose a course to assign student: "))
        if choose > len(courses_list) or choose < 1:
            print('Invalid course')
        else:
            course_student[choose-1].extend(assign_students(students_list))
            for i in range (len(course_student[choose-1])):
                course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"] = None


def show_course_student(courses_list,number_course, course_student):
    if len(courses_list) == 0:
        print("please input courses information")
    else:
        show_courses(courses_list, number_course)   
        choose = int(input("Choose course: "))
        if choose > len(courses_list) or choose < 1:
            print('Invalid course')
        else:
            if len(course_student[choose-1]) == 0:
                print("No student in the course")
            else:
                print('Student in course:')
                for i in range (len(course_student[choose-1])):
                    print(f"{i+1} | ID: {course_student[choose-1][i]['Student ID']} | FULL NAME: {course_student[choose-1][i]['Full name']} | DATE OF BIRTH: {course_student[choose-1][i]['DoB']} |")


def input_mark(course_student, courses_list, number_course):
    if len(courses_list) == 0:
        print("please input course information")
    else:
        show_courses(courses_list,number_course)
        choose = int(input("Choose the course to input: "))
        if choose > len(courses_list) or choose < 1:
            print('Invalid course')
        else:
            if len(course_student[choose-1]) == 0:
                print("No student in the course")
            else:
                for i in range (len(course_student[choose-1])):
                    if course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"] == None:
                        print(f"{i+1} | ID: {course_student[choose-1][i]['Student ID']} | FULL NAME: {course_student[choose-1][i]['Full name']} | DATE OF BIRTH: {course_student[choose-1][i]['DoB']} |")
                    else:
                        print(f"""{i+1} | ID: {course_student[choose-1][i]['Student ID']} | FULL NAME: {course_student[choose-1][i]['Full name']} | DATE OF BIRTH: {course_student[choose-1][i]['DoB']} | {f"Mark_{courses_list[choose-1]['Course name']}"}: {course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"]}""")

                choose_student =input("input for student (Student ID): ")
                exist = False   
                for i in range (len(course_student[choose-1])):
                    if choose_student == course_student[choose-1][i]['Student ID']:
                        exist = True
                        mark = float(input("Mark: "))
                        course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"] = mark
                if exist == False:
                    print(f"ID {choose_student} does not exist")


def show_course_mark(course_student,courses_list, number_course):
    if len(courses_list) == 0:
        print("Please input courses information")
    else:
        show_courses(courses_list,number_course)
        choose = int(input("Choose course: "))
        if choose > len(courses_list) or choose < 1:
            print('Invalid course')
        else:
            if len(course_student[choose-1]) != 0:           
                for i in range (len(course_student[choose-1])):
                    if course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"] != None:
                        print(f"""{i+1} | ID: {course_student[choose-1][i]['Student ID']} | FULL NAME: {course_student[choose-1][i]['Full name']} | {f"Mark_{courses_list[choose-1]['Course name']}"}: {course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"]}""")
                    else:
                        print(f"""{i+1} | ID: {course_student[choose-1][i]['Student ID']} | FULL NAME: {course_student[choose-1][i]['Full name']} | {f"Mark_{courses_list[choose-1]['Course name']}"}: No input | """)

            else:
                print("No student in the course")




def main():
    students_list = []
    courses_list = []
    number_student = None
    number_course = None
    course_student = []
    # input number of student
    while True:
        print("\n________________OPTIONS_________________")
        print("0. Close the program")
        print("1. Input number of student")
        print("2. input student information (ID, name, DoB)")
        print("3. Input number of courses")
        print("4. input courses information (ID, course name)")
        print("5. Assign students to courses")
        print("6. input student mark in course")
        print("7. print student list")
        print("8. print course list")
        print("9. print list student in each course")
        print("10. print students mark in each course")
              
        choose = input("Option: ")
        if choose == '0':
            break

        elif choose == '1':
            print("\n---------------------------")
            number_student = number_students()
            print("---------------------------")

        elif choose == '2':
            print("\n---------------------------")
            print("Input students information:")
            if number_student == None:
                print("Please input number of student")
            else:
                for _ in range (number_student):
                    print(f"Student {_+1}:")
                    students_list.append(input_students())
                    print("\n")
            print("---------------------------")

        elif choose == '3':
            print("\n---------------------------")
            number_course = number_courses()
            print("---------------------------")
            course_student = [[] for _ in range(number_course)]

        elif choose == '4':
            print("\n---------------------------")
            print("Input course information: ")
            if number_course == None:
                print("Please input number of course")
            else:
                for _ in range (number_course):
                    print(f"Course {_+1}:")
                    courses_list.append(input_course())
                    print("\n")
            print("---------------------------")

        elif choose == '5':
            print("\n---------------------------")
            print("Assign student into courses")
            choose_course(courses_list,number_course, students_list, course_student)
            print("---------------------------")

        elif choose == '6':
            print("\n---------------------------")
            print("Input mark in each course")
            input_mark(course_student, courses_list, number_course)
            print("---------------------------")

        elif choose == '7':
            print("\n---------------------------")
            print("Print student list")
            show_students(students_list,number_student)
            print("---------------------------")

        elif choose == '8':
            print("\n---------------------------")
            print("Print course list")
            show_courses(courses_list, number_course)
            print("---------------------------")

        elif choose == '9':
            print("\n---------------------------")
            print("Print list student in each course")
            show_course_student(courses_list,number_course, course_student)
            print("---------------------------")

        elif choose == '10':
            print("\n---------------------------")
            print("Print students mark in each course")
            show_course_mark(course_student,courses_list, number_course)
            print("---------------------------")

        else:
            print("\n---------------------------")
            print("Not valid option\nPlease input again")
            print("---------------------------")




if __name__ == "__main__":
    main()



