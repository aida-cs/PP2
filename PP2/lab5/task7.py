import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def snake_to_camel(text):
    return ''.join(word.capitalize() for word in text.split('_'))