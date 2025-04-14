import csv

def delete_student(filename):
    deleted = False
    students = []

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        students.append(header)

        data = [row for row in reader if row]

    print("Delete by:")
    print("1. Name contains")
    print("2. Phone equals")
    print("3. Year equals")
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

delete_student("students.csv")
if __name__ == "__main__":
    pass