import pyodbc


# database connection
server = r'DESKTOP-F6BQ6H9\MSSQL'
database = 'student_management'

connection = pyodbc.connect(
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
    f'TrustServerCertificate=yes;'
)

cursor = connection.cursor()


# calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "a+"
    elif marks >= 80:
        return "a"
    elif marks >= 70:
        return "b"
    elif marks >= 60:
        return "c"
    else:
        return "d"


# add student
def add_student():
    print("\n--- add student ---")

    name = input("enter student name: ")
    age = int(input("enter student age: "))
    course = input("enter course: ")
    marks = float(input("enter marks: "))

    grade = calculate_grade(marks)

    query = """
    insert into students (name, age, course, marks, grade)
    values (?, ?, ?, ?, ?)
    """

    cursor.execute(query, (name, age, course, marks, grade))
    connection.commit()

    print("\nstudent added successfully!")
    print(f"grade: {grade}")


# view all students
def view_students():
    print("\n--- student records ---")

    cursor.execute("select * from students")
    students = cursor.fetchall()

    if not students:
        print("no student records found!")
        return

    print("-" * 90)

    for student in students:
        print(
            f"id: {student.student_id} | "
            f"name: {student.name} | "
            f"age: {student.age} | "
            f"course: {student.course} | "
            f"marks: {student.marks} | "
            f"grade: {student.grade}"
        )

    print("-" * 90)


# search student
def search_student():
    print("\n--- search student ---")

    student_id = int(input("enter student id: "))

    query = "select * from students where student_id = ?"

    cursor.execute(query, (student_id,))
    student = cursor.fetchone()

    if student:
        print("\nstudent found!")
        print("-" * 50)
        print(f"id: {student.student_id}")
        print(f"name: {student.name}")
        print(f"age: {student.age}")
        print(f"course: {student.course}")
        print(f"marks: {student.marks}")
        print(f"grade: {student.grade}")
        print("-" * 50)
    else:
        print("student not found!")


# update student
def update_student():
    print("\n--- update student ---")

    student_id = int(input("enter student id: "))

    cursor.execute(
        "select * from students where student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\ncurrent details:")
        print(f"name: {student.name}")
        print(f"age: {student.age}")
        print(f"course: {student.course}")
        print(f"marks: {student.marks}")

        name = input("\nenter new name: ")
        age = int(input("enter new age: "))
        course = input("enter new course: ")
        marks = float(input("enter new marks: "))

        grade = calculate_grade(marks)

        query = """
        update students
        set name = ?, age = ?, course = ?, marks = ?, grade = ?
        where student_id = ?
        """

        cursor.execute(
            query,
            (name, age, course, marks, grade, student_id)
        )

        connection.commit()

        print("\nstudent updated successfully!")
    else:
        print("student not found!")


# delete student
def delete_student():
    print("\n--- delete student ---")

    student_id = int(input("enter student id: "))

    cursor.execute(
        "select * from students where student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nstudent found!")
        print(f"name: {student.name}")
        print(f"course: {student.course}")

        confirm = input(
            "are you sure you want to delete this student? (yes/no): "
        )

        if confirm.lower() == "yes":
            cursor.execute(
                "delete from students where student_id = ?",
                (student_id,)
            )

            connection.commit()

            print("student deleted successfully!")
        else:
            print("delete operation cancelled!")
    else:
        print("student not found!")


# main menu
while True:
    print("\n===================================")
    print("       student management system")
    print("===================================")
    print("1. add student")
    print("2. view students")
    print("3. search student")
    print("4. update student")
    print("5. delete student")
    print("6. exit")
    print("===================================")

    choice = input("enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nthank you for using student management system!")
        break

    else:
        print("\ninvalid choice! please try again.")


connection.close()