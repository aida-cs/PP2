import csv

def add_student(filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        while True:
            newline = '\n'
            name = input("Enter name (or 'q' to quit): ")
            if name.lower() == 'q':
                break
            telephone = input("Enter telephone number: ")
            year = input("Enter year: ")
            writer.writerow([newline, name, telephone, year])
            print("Student added!\n")

add_student("students.csv")
if __name__ == "__main__":
    pass