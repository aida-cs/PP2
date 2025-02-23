import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def camel_to_snake(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()