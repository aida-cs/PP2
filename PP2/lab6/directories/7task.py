import shutil

source = input("Enter source file: ")
destination = input("Enter destination file: ")
shutil.copyfile(source, destination)