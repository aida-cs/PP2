import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def match_a_b(text):
    return re.findall(r'a{1}b*', text)