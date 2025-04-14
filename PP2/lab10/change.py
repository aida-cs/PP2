import csv

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
                print("What do you want to update?")
                print("1. Name")
                print("2. Phone")
                print("3. Year")
                choice = input("Enter 1, 2, or 3: ")

                if choice == '1':
                    row[0] = input("Enter new name: ")
                elif choice == '2':
                    row[1] = input("Enter new phone number: ")
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

update_student("students.csv")
if __name__ == "__main__":
    pass