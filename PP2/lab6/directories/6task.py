import os

directory = input("Enter the directory name: ")
os.makedirs(directory, exist_ok=True)
[open(f"{directory}/{chr(c)}.txt", 'w').write(f"This is {chr(c)}.txt\n") for c in range(65, 91)]