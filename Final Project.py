import random

students_list = []
courses = []


class Course:
    def __init__(self, a, b, d):
        self.course_id = a
        self.course_name = b
        self.course_class = d

    def get_course_details(self):
        print("Course_id    |", self.course_id)
        print("course_name  |", self.course_name)
        print("course_class |", self.course_class.upper())
        print(" ******")


class Students:
    def __init__(self, e, g):
        self.student_name = e
        self.student_id = random.randint(10000, 99999)
        self.student_class = g
        self.student_courses = []

    def add_course(self, course):
        if self.student_class == course.course_class:
            self.student_courses.append(course.course_name)
            print("course saved successfully")
        else:
            print("Student class or Course class not found")

    def display_student_details(self):
        print("id      |", self.student_id)
        print("Name    |", self.student_name)
        print("Class   |", self.student_class.upper())
        print("courses |", self.student_courses)
        print(" ******")


while True:
    print("Select choice please")
    print("1. Add new student")
    print("2. Remove student")
    print("3. Edit student")
    print("4. Display all students")
    print("5. Display all courses")
    print("6. Create new course")
    print("7. Add course to student")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 0:
        exit()

    elif choice == 1:
        student_name = str(input('inter student name: '))
        student_class = str(input('inter course class(A-B-C): '))
        while student_class.upper() not in ["A", 'B', 'C']:
            student_class = str(input('inter course class(A-B-C): '))
        new_student = Students(student_name, student_class)
        students_list.append(new_student)
        print("Student saved successfully")

    elif choice == 2:
        student_id = int(input('inter student id: '))
        bd = False
        for i in students_list:
            if i.student_id == student_id:
                bd = True
                students_list.remove(i)
                print('delete done successful')
        if not bd:
            print('user not exist')

    elif choice == 3:
        c = int(input('inter student id: '))
        bx = False
        for i in students_list:
            if i.student_id == c:
                bx = True
                i.student_name = str(input('inter student name: '))
                i.student_class = str(input('inter course class(A-B-C): '))
                while student_class.upper() not in ["A", 'B', 'C']:
                    student_class = str(input('inter course class(A-B-C): '))
                print("Student edited successfully")
        if not bx:
            print('user not exist')

    elif choice == 4:
        for display in students_list:
            display.display_student_details()

    elif choice == 5:
        for dis in courses:
            dis.get_course_details()

    elif choice == 6:
        course_id = int(input('enter course id (must be a number): '))
        course_name = str(input('enter course name: '))
        course_class = str(input('inter course class(A-B-C): '))
        while course_class.upper() not in ["A", 'B', 'C']:
            course_class = str(input('inter course class(A-B-C): '))
        new_course = Course(course_id, course_name, course_class)
        courses.append(new_course)

    elif choice == 7:
        x = int(input('inter student id: '))
        bs = False
        for i in students_list:
            if i.student_id == x:
                bs = True
        if not bs:
            print("user not exist")
        else:
            course_name = input('enter course name: ')
            bc = False
            for f in courses:
                if f.course_name.strip().lower() == course_name.strip().lower():
                    bc = True
                    break
            if not bc:
                print("course not exist")
            else:
                if i.student_class.upper() == f.course_class.upper():
                    i.add_course(f)
                    print('course added')
                else:
                    print("Student class and course class do not match")
