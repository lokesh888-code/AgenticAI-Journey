class StudentFileManager:
    """A class to manage student records in a file."""
    
    def __init__(self, filename="students.txt"):
        """Initialize the StudentFileManager with a filename."""
        self.filename = filename
    
    def add_student(self, name):
        """Add a student name to the file."""
        try:
            with open(self.filename, 'a') as file:
                file.write(name + '\n')
            print(f" Student '{name}' added successfully!")
        except IOError as e:
            print(f"Error adding student: {e}")
    
    def view_students(self):
        """Read and display all students from the file."""
        try:
            with open(self.filename, 'r') as file:
                students = file.readlines()
            
            if not students:
                print("No students found in the file.")
            else:
                print("\n" + "="*40)
                print("STUDENT LIST")
                print("="*40)
                for i, student in enumerate(students, 1):
                    print(f"{i}. {student.strip()}")
                print("="*40)
                print(f"Total students: {len(students)}")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found!")
            print("Please add some students first.")
        except IOError as e:
            print(f"Error reading file: {e}")
    
    def search_student(self, search_name):
        """Search for a student in the file."""
        try:
            with open(self.filename, 'r') as file:
                students = file.readlines()
            
            found = False
            print("\n" + "="*40)
            print(f" SEARCH RESULTS FOR: '{search_name}'")
            print("="*40)
            
            for i, student in enumerate(students, 1):
                if search_name.lower() in student.lower():
                    print(f"{i}. {student.strip()}")
                    found = True
            
            if found:
                print("="*40)
                print(f" Found '{search_name}' in the file!")
            else:
                print(f" Student '{search_name}' not found.")
                print("="*40)
                
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found!")
            print("Please add some students first.")
        except IOError as e:
            print(f"Error searching file: {e}")
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*40)
        print("🎓 STUDENT FILE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        print("="*40)


def main():
    """Main function to run the Student File Management System."""
    # Create an object of the StudentFileManager class
    manager = StudentFileManager()
    
    while True:
        manager.display_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                name = input("Enter student name: ").strip()
                if name:
                    manager.add_student(name)
                else:
                    print("Student name cannot be empty!")
            
            elif choice == '2':
                manager.view_students()
            
            elif choice == '3':
                search_name = input("Enter student name to search: ").strip()
                if search_name:
                    manager.search_student(search_name)
                else:
                    print("Search name cannot be empty!")
            
            elif choice == '4':
                print("\nThank you for using Student File Management System!")
                print("Goodbye!\n")
                break
            
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        
        except KeyboardInterrupt:
            print("\n\n Program interrupted by user.")
            print(" Goodbye!\n")
            break
        except EOFError:
            print("\n\n End of input reached.")
            print(" Goodbye!\n")
            break


if __name__ == "__main__":
    main()