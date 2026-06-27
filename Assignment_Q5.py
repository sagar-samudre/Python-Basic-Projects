# Q5: Student Database
def student_database():
    students = {}
    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            try:
                roll = input("Roll Number: ")
                name = input("Name: ")
                age = int(input("Age: "))
                city = input("City: ")
                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student Added Successfully.")

            except ValueError:
                print("Invalid Age.")
        elif choice == "2":
            roll = input("Enter Roll Number: ")
            data = students.get(roll)

            if data:
                print(data)
            else:
                print("Student Not Found.")
        elif choice == "3":
            if len(students) == 0:
                print("No Records Found.")
            else:
                for roll, details in students.items():
                    print("\nRoll:", roll)
                    print(details)
        elif choice == "4":
            print("Program Ended.")
            break
        else:
            print("Invalid Choice.")
student_database()