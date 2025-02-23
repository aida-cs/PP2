import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def find_capitalized_words(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)