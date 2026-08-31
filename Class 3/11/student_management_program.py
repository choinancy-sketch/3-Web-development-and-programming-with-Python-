import json
import os

# File to store persistent student data
DATA_FILE = "students_data.json"

def load_data():
    """Loads student records from the JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading data file. Starting with an empty database.")
            return {}
    return {}

def save_data(students):
    """Saves student records dictionary to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    """Adds a new student to the database."""
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID (e.g., S101): ").strip()
    
    if not student_id:
        print("Student ID cannot be empty.")
        return
    
    if student_id in students:
        print(f"Error: A student with ID '{student_id}' already exists.")
        return

    name = input("Enter Full Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: ").strip())
        grade = float(input("Enter GPA / Grade (e.g., 3.8): ").strip())
    except ValueError:
        print("Invalid input! Age must be an integer and grade must be a number.")
        return

    department = input("Enter Department/Program: ").strip()

    # Store student details in a nested dictionary
    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "department": department if department else "General"
    }
    
    save_data(students)
    print(f"Success: Student {name} ({student_id}) added successfully!")

def view_students(students):
    """Displays all registered students in a formatted layout."""
    print("\n--- Student Roster ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'ID':<10} | {'Name':<20} | {'Age':<5} | {'Grade':<6} | {'Department':<15}")
    print("-" * 65)
    for s_id, info in students.items():
        print(f"{s_id:<10} | {info['name']:<20} | {info['age']:<5} | {info['grade']:<6.2f} | {info['department']:<15}")

def search_student(students):
    """Searches for a student by ID or Name."""
    print("\n--- Search Student ---")
    keyword = input("Enter Student ID or Name to search: ").strip().lower()
    
    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False
    print(f"{'ID':<10} | {'Name':<20} | {'Age':<5} | {'Grade':<6} | {'Department':<15}")
    print("-" * 65)
    
    for s_id, info in students.items():
        if keyword in s_id.lower() or keyword in info['name'].lower():
            print(f"{s_id:<10} | {info['name']:<20} | {info['age']:<5} | {info['grade']:<6.2f} | {info['department']:<15}")
            found = True

    if not found:
        print("No matching student records found.")

def update_student(students):
    """Updates an existing student's grade or department."""
    print("\n--- Update Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()
    
    if student_id not in students:
        print(f"Error: Student with ID '{student_id}' not found.")
        return

    print(f"Updating record for: {students[student_id]['name']}")
    print("1. Update Grade")
    print("2. Update Department")
    choice = input("Select option (1-2): ").strip()

    if choice == '1':
        try:
            new_grade = float(input("Enter new Grade/GPA: ").strip())
            students[student_id]['grade'] = new_grade
            save_data(students)
            print("Grade updated successfully!")
        except ValueError:
            print("Invalid grade format. Must be a number.")
    elif choice == '2':
        new_dept = input("Enter new Department: ").strip()
        students[student_id]['department'] = new_dept if new_dept else "General"
        save_data(students)
        print("Department updated successfully!")
    else:
        print("Invalid choice.")

def delete_student(students):
    """Deletes a student record by ID."""
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Student ID to delete: ").strip()
    
    if student_id not in students:
        print(f"Error: Student with ID '{student_id}' not found.")
        return

    confirm = input(f"Are you sure you want to delete {students[student_id]['name']}? (y/n): ").strip().lower()
    if confirm == 'y':
        del students[student_id]
        save_data(students)
        print("Student record deleted successfully.")
    else:
        print("Deletion cancelled.")

def main():
    """Main program execution loop."""
    students = load_data()
    
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM  ")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Record")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("\nThank you for using the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()