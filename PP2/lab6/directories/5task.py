file_path = input("Enter the file path: ")
items = input("Enter list items separated by commas: ").split(',')
open(file_path, 'w', encoding='utf-8').writelines(f"{item.strip()}\n" for item in items)