def read_file_to_dict(filename):
    student_dict = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, grade = parts[0].strip(), parts[1].strip()
                    student_dict[name] = float(grade)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty dictionary.")
    return student_dict


def add_student(student_dict, name, grade):
    student_dict[name] = grade
    print(f"Added student: {name} with grade {grade}")


def calculate_average(student_dict):
    if not student_dict:
        print("No student data available to calculate average.")
        return None
    total = sum(student_dict.values())
    return total / len(student_dict)


def print_above_average_students(student_dict, average):
    print("\nStudents scoring above average:")
    for name, grade in student_dict.items():
        if grade > average:
            print(f"{name}: {grade}")


# Main program
if __name__ == "__main__":
    filename = "students.txt"
    students = read_file_to_dict(filename)

    while True:
        print("\nOptions:")
        print("1. Add new student data")
        print("2. Calculate average grade")
        print("3. Print students who scored above average")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = float(input("Enter student grade: "))
            add_student(students, name, grade)

        elif choice == "2":
            average = calculate_average(students)
            if average is not None:
                print(f"Average grade: {average:.2f}")

        elif choice == "3":
            average = calculate_average(students)
            if average is not None:
                print_above_average_students(students, average)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
