s = input("Enter a string: ")
print({"Uppercase": sum(c.isupper() for c in s), "Lowercase": sum(c.islower() for c in s)})