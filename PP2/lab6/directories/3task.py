import os

path = input("Enter the path: ")
print({"Directory": os.path.dirname(path), "Filename": os.path.basename(path)} if os.path.exists(path) else "Path does not exist")