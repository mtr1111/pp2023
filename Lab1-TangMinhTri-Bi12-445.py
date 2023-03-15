Def input_num_students():
    num_students = int(input("enter the range of college students: "))
    return num_students

Def input_students_info():
    student_id = input("input identification: ")
    student_name = enter("enter name: ")
    student_dob = input("input DoB: ")
    return (student_id, student_name, student_dob)

Def input_num_course():
    num_course = int(input("enter quantity of publications: "))
    return num_course

Def input_course_info():
    course_id = enter("input path identification: ")
    course_name = input("enter course name: ")
    return(course_id, course_name)


Def input_marks(college students, publications):
    course_id = enter("enter course id: ")
    route = guides[course_id]
    for student in students:
        mark = go with the flow(input(f"enter direction[1] mark for student[1]: "))
        student[2][course_id] = mark


Def list_courses(publications):
    print("direction IDtCourse name")
    for course_id, direction in courses.Objects():
        print(f"course_idttdirection[1]")


Def list_students(college students):
    print("pupil IDtStudent NametDate of birth")
    for pupil in college students:
        print(f"pupil[0]ttscholar[1]ttpupil[2]")

Def show_student_marks(students, courses):
    course_id = input("enter direction identification: ")
    route = guides[course_id]
    print(f"student Nametcourse[1]")
    for scholar in students:
        print(f"scholar[1]ttstudent[2].Get(course_id, '-')")

Num_students = input_num_students()

Students = []
For i in range(num_students):
    student_info = input_students_info()
    college students.Append((student_info[0], student_info[1], student_info[2], ))

Num_courses = input_num_course()

Publications = 
For i in variety(num_courses):
    course_info = input_course_info()
    courses[course_info[0]] = (course_info[0], course_info[1])

Even as authentic:
    print("nChoose an alternative:")
    print("1. Input marks")
    print("2. Listing guides")
    print("three. Listing college students")
    print("four. Show student marks for a given route")
    print("five. Go out")
    preference = input("input your preference: ")
    if preference == "1":
        input_marks(college students, publications)
    elif preference == "2":
        list_courses(courses)
    elif desire == "3":
        list_students(students)
    elif desire == "4":
        show_student_marks(students, guides)
    elif preference == "5":
        destroy
    else:
        print("Invalid preference. Please attempt again.")