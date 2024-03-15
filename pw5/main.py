from input import  number_students, number_courses, input_student, input_course, choose_course, input_mark, write_courses, write_mark, write_students,compress_files,decompress_files
from output import show_students, show_courses, show_course_student, show_mark, show_gpa, sorting_gpa
from domain.university import University

def main():
    u = University()
    decompress = input("Decompress student.dat (y/n)?")
    if decompress == "y":
        try:
            decompress_files(u.student_list,u.course_list)
            print("Decompress and load successful")
            u.course_student = [[] for _ in range(len(u.course_list))]
        except FileNotFoundError:
            print("Student.dat does not exist")
    while True:
        print("\n________________OPTIONS_________________")
        print("0. Close the program")
        print("1. Input student information (ID, name, DoB)")
        print("2. Input courses information (ID, course name)")
        print("3. Assign students to courses")
        print("4. input student mark for courses")
        print("5. print student list")
        print("6. print course list")
        print("7. print list student in each course")
        print("8. print students mark in each course")
        print("9. Print GPA")
        print("10. Sorting GPA")

        choose = input("Option: ")
        if choose == '0':
            write_students(u.student_list)
            write_courses(u.course_list)
            write_mark(u.student_list)
            compress_files()
            break

        elif choose == '1':
            print("\n---------------------------")
            number_student = number_students()
            print("---------------------------")
            print("\n---------------------------")
            print("Input students information:")
            if number_student == None:
                print("Please input number of student")
            else:
                for _ in range (number_student):
                    print(f"Student {_+1}:")
                    u.student_list.append(input_student())
                    print("\n")
            print("---------------------------")

        elif choose == '2':
            print("\n---------------------------")
            number_course = number_courses()
            print("---------------------------")
            u.course_student = [[] for _ in range(len(u.course_list))]
            print("\n---------------------------")
            print("Input course information: ")
            if number_course == None:
                print("Please input number of course")
            else:
                for _ in range (number_course):
                    print(f"Course {_+1}:")
                    u.course_list.append(input_course())
                    print("\n")
            print("---------------------------")

        elif choose == '3':
            print("\n---------------------------")
            print("Assign student into courses")
            choose_course(u.course_list, u.student_list, u.course_student)
            print("---------------------------")
        
        elif choose == '4':
            print("\n---------------------------")
            print("Input marks for each course")
            input_mark(u.course_list, u.course_student)
            print("---------------------------")


        elif choose == '5':
            print("\n---------------------------")
            print("Print student list")
            show_students(u.student_list)
            print("---------------------------")

        elif choose == '6':
            print("\n---------------------------")
            print("Print course list")
            show_courses(u.course_list)
            print(len(u.course_list))
            print("---------------------------")
        
        elif choose == '7':
            print("\n---------------------------")
            print("Print students in each course")
            print("---------------------------")
            show_course_student(u.course_list,u.course_student)
            print("---------------------------")

        elif choose == '8':
            print("\n---------------------------")
            print("Print students mark in each course")
            print("---------------------------")
            show_mark(u.course_list,u.student_list,u.course_student)
            print("---------------------------")

        elif choose == '9':
            print("\n--------------------------")
            print("Calculate student result")
            print("---------------------------")
            show_gpa(u.student_list,u.course_list)
            print("---------------------------")
        
        elif choose == '10':
            print("\n--------------------------")
            print("Sorting gpa by decending order")
            print("---------------------------")
            sorting_gpa(u.student_list,u.course_list)
            print("---------------------------")
      
        else:
            print("\n---------------------------")
            print("Not valid option\nPlease input again")
            print("---------------------------")

if __name__ == "__main__":
    main()
