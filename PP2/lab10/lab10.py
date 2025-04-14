import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="650280"
)

FILENAME = "students.csv"

# Add student(s) interactively
def add_student(filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        while True:
            name = input("Enter name (or 'q' to quit): ")
            if name.lower() == 'q':
                break
            telephone = input("Enter telephone number: ")
            year = input("Enter year: ")
            writer.writerow([name, telephone, year])
            print("Student added!\n")

# Update student info (name, phone, or year)
def update_student(filename):
    updated = False
    students = []

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        students.append(header)

        for row in reader:
            if not row:
                continue
            name, phone, year = row
            if input(f"Do you want to update '{name}'? (y/n): ").lower() == 'y':
                print("1. Name\n2. Phone\n3. Year")
                choice = input("Enter 1, 2, or 3: ")

                if choice == '1':
                    row[0] = input("Enter new name: ")
                elif choice == '2':
                    row[1] = input("Enter new phone: ")
                elif choice == '3':
                    row[2] = input("Enter new year: ")
                else:
                    print("Invalid choice.")
                    continue

                updated = True
            students.append(row)

    if updated:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print("Student(s) updated successfully.")
    else:
        print("No updates made.")

# Delete student(s) by name, phone, or year
def delete_student(filename):
    deleted = False
    students = []

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        students.append(header)
        data = [row for row in reader if row]

    print("Delete by:\n1. Name contains\n2. Phone equals\n3. Year equals")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        keyword = input("Enter part of the name: ").lower()
        filtered = [row for row in data if keyword not in row[0].lower()]
    elif choice == '2':
        phone = input("Enter exact phone number: ")
        filtered = [row for row in data if row[1] != phone]
    elif choice == '3':
        year = input("Enter year to delete: ")
        filtered = [row for row in data if row[2] != year]
    else:
        print("Invalid choice.")
        return

    if len(filtered) < len(data):
        students.extend(filtered)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print("Student(s) deleted successfully.")
    else:
        print("No matching student(s) found to delete.")

# Query students by name, phone, or year
def query_students(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader if row]

    print("Query by:\n1. Name contains\n2. Phone equals\n3. Year equals")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        keyword = input("Enter name keyword: ").lower()
        result = [row for row in data if keyword in row[0].lower()]
    elif choice == '2':
        phone = input("Enter exact phone number: ")
        result = [row for row in data if row[1] == phone]
    elif choice == '3':
        year = input("Enter year: ")
        result = [row for row in data if row[2] == year]
    else:
        print("Invalid choice.")
        return

    if result:
        print("\nResults:")
        print(header)
        for row in result:
            print(row)
    else:
        print("No matching students found.")

# Main menu
def main():
    while True:
        print("\n--- STUDENT DATABASE MENU ---")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Query students")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == '1':
            add_student(FILENAME)
        elif choice == '2':
            update_student(FILENAME)
        elif choice == '3':
            delete_student(FILENAME)
        elif choice == '4':
            query_students(FILENAME)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()