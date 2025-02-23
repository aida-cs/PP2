import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def split_at_uppercase(text):
    return re.split(r'(?=[A-Z])', text)