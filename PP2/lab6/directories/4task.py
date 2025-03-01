file_path = input("Enter the file path: ")
print(sum(1 for _ in open(file_path, encoding='utf-8')))