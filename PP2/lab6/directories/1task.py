import os

path = input("Enter the path: ")
print({
    "Directories": [d for d in os.listdir(path) if os.path.isdir(d)],
    "Files": [f for f in os.listdir(path) if os.path.isfile(f)],
    "All": os.listdir(path)
})