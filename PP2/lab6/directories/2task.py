import os

path = input("Enter the path: ")
print({perm: os.access(path, mode) for perm, mode in zip(["Exists", "Readable", "Writable", "Executable"], [os.F_OK, os.R_OK, os.W_OK, os.X_OK])})