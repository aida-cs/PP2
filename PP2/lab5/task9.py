import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def insert_spaces_capitals(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)