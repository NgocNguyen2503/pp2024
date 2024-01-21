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
    print("input assigned student ")
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
    show_courses(courses_list, number_course)   
    choose = int(input("Choose a course to assign student: "))
    if choose > len(courses_list):
        print('Invalid course')
    else:
        course_student[choose-1].extend(assign_students(students_list))
        for i in range (len(course_student[choose-1])):
            course_student[choose-1][i][f"Mark_{courses_list[choose-1]['Course name']}"] = None


def show_course_student(courses_list,number_course, course_student):
    show_courses(courses_list, number_course)   
    choose = int(input("Choose course: "))
    if choose > len(courses_list) and choose < 1:
        print('Invalid course')
    else:
        print('Student in course:')
        for i in range (len(course_student[choose-1])):
            print(f"{i+1} | ID: {course_student[choose-1][i]['Student ID']} | FULL NAME: {course_student[choose-1][i]['Full name']} | DATE OF BIRTH: {course_student[choose-1][i]['DoB']} |")


def input_mark(course_student, courses_list, number_course):
    show_courses(courses_list,number_course)
    choose = int(input("Choose the course to input: "))
    if choose > len(courses_list) and choose < 1:
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
    show_courses(courses_list,number_course)
    choose = int(input("Choose course: "))
    if choose > len(courses_list) and choose < 1:
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
    # input number of student
    number_student = number_students() 
    # input information for student
    for _ in range (number_student):
        students_list.append(input_students())
    show_students(students_list,number_student)

    
    #input number of course
    number_course = number_courses()
    #course_student = [None] * number_course
    course_student = [[] for _ in range(number_course)]
    #input courses information
    for _ in range (number_course):
        courses_list.append(input_course())
    show_courses(courses_list, number_course)
    choose_course(courses_list,number_course, students_list, course_student)
    choose_course(courses_list,number_course, students_list, course_student)
    show_course_student(courses_list,number_course, course_student)
    choose_course(courses_list,number_course, students_list, course_student)
    show_course_student(courses_list,number_course, course_student)
    input_mark(course_student, courses_list, number_course)
    input_mark(course_student, courses_list, number_course)
    input_mark(course_student, courses_list, number_course)
    show_course_student(courses_list,number_course, course_student)
    show_course_mark(course_student,courses_list, number_course)
    show_course_mark(course_student,courses_list, number_course)

        

if __name__ == "__main__":
    main()



