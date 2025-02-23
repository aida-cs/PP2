import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def find_underscore_words(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)