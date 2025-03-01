import os

path = input("Enter the file path to delete: ")
if os.access(path, os.W_OK) and os.remove(path) is None:
    print("File deleted successfully")
else:
    print("File does not exist or is not writable")