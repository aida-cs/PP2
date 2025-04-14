import csv

def query_students(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader if row]

    print("Choose a filter:")
    print("1. Name contains")
    print("2. Phone equals")
    print("3. Year equals")
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

query_students("students.csv")
if __name__ == "__main__":
    pass