def student_grade_management():

    student_grades = {}
    
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add a new student and grade")
        print("2. Update an existing student's grade")
        print("3. Print all student grades")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            
            if name in student_grades:
                print(f"Student '{name}' already exists. Use update option to change grade.")
                continue
                
            try:
                grade = float(input("Enter student grade: "))
                student_grades[name] = grade
                print(f"Student '{name}' with grade {grade} added successfully.")
            except ValueError:
                print("Invalid grade. Please enter a number.")
        
        elif choice == "2":
            name = input("Enter student name to update: ")
            
            
            if name not in student_grades:
                print(f"Student '{name}' not found in the system.")
                continue
                
         
            try:
                new_grade = float(input("Enter new grade: "))
                student_grades[name] = new_grade
                print(f"Grade for '{name}' updated to {new_grade} successfully.")
            except ValueError:
                print("Invalid grade. Please enter a number.")
        
      
        elif choice == "3":
            if not student_grades:
                print("No students in the system yet.")
            else:
                print("\n----- Student Grades -----")
                for student, grade in student_grades.items():
                    print(f"{student}: {grade}")
        
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    student_grade_management()