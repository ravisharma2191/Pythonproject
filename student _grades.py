
students = {}
while True:
    print("\n--- Student Grades Manager ---")
    print("1. Add new student and grade")
    print("2. Update existing student’s grade")
    print("3. Print all student grades")
    print("4. Remove existing student’s")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        
        if name in students:
            print("Student already exists!")
        else:
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found!")

    elif choice == "3":
        if not students:
            print("No students found.")
        else:
            print("\n--- Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")

    elif choice == "4":
        name = input("Enter student name to update: ")
        
        if name in students:
             del students[name]
             
             print(" Remove successfully.")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
