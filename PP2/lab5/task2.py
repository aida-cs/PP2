import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def match_a_b2_3(text):
    return re.findall(r'a{1}b{2,3}', text)