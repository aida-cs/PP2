import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def replace_special_chars(text):
    return re.sub(r'[ ,.]', ':', text)