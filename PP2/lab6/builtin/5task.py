t = tuple(map(lambda x: x.lower() == "true", input("Enter boolean values (True/False) separated by spaces: ").split()))
print(all(t))