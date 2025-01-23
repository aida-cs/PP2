print(bool("Hello"))
print(bool(15))  #Python Booleans

print((6 + 3) - (6 + 3))  #Python Operators

#Python Lists:

    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)  #Python Lists

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  #Access list items
    print(thislist[1])  #print second item with index '1'
    print(thislist[2:5])  #print third, fourth, fifth elements, from index '2' to '5' not included

    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"  #Change the second item:
    thislist[1:3] = ["blackcurrant", "watermelon"]  #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
    thislist[1:2] = ["blackcurrant", "watermelon"]  #Change the second value by replacing it with two new values:
    print(thislist)  #Change list items

    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")  #Add new element to the list
    print(thislist)
    thislist.insert(1, "orange")  #Insert an item as the second position:
    print(thislist)  #Add list items

    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    thislist.pop(1)  #The pop() method removes the specified index.
    print(thislist)  #Remove list items

#Loop lists:

    thislist = ["apple", "banana", "cherry"]
    for i in range(len(thislist)):
        print(thislist[i])

    thislist = ["apple", "banana", "cherry"]
    i = 0
    while i < len(thislist):
        print(thislist[i])
        i = i + 1

    #List Comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]  #newlist = [expression for item in iterable if condition == True]
    print(newlist)

    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()  #Sort list
    thislist.reverse()  #Reverse the list
    thislist.sort(reverse = True)  #Sort the list descending:
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)  #Copy lists

    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)  #Join Lists

#Python Tuples:

    thistuple = ("apple", "banana", "cherry")
    print(thistuple)  #Python Tuples

    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])  #Access Tuple

    #Update tuples:
        thistuple = ("apple", "banana", "cherry")
        y = list(thistuple)  #Convert the tuple into a list, add "orange", and convert it back into a tuple:
        y.append("orange") 
        thistuple = tuple(y)  #Update tuples

        thistuple = ("apple", "banana", "cherry")
        y = ("orange",)
        thistuple += y  #Create a new tuple with the value "orange", and add that tuple:
        print(thistuple)

    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits  #Unpacking tuple
    print(green)
    print(yellow)
    print(red)

    thistuple = ("apple", "banana", "cherry")  #Loop tuples
    for i in range(len(thistuple)):
        print(thistuple[i])

    tuple1 = ("a", "b" , "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2  #Join tuples
    print(tuple3)

#Python Sets:

    thisset = {"apple", "banana", "cherry"}  #Python sets
    print(thisset)

    thisset = {"apple", "banana", "cherry"}
    for x in thisset:  #Access set items
        print(x)

    thisset = {"apple", "banana", "cherry"}
    mylist = ["kiwi", "orange"]  #The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
    thisset.update(mylist)
    thisset.add("orange")  #Add set items
    print(thisset)

    thisset = {"apple", "banana", "cherry"}
    thisset.remove("banana")  #Rempve set items
    print(thisset)

    thisset = {"apple", "banana", "cherry"}
    for x in thisset:  #Loop through the set, and print the values:
        print(x)

    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)  #Join set1 and set2 into a new set:
    set3 = set1.intersection(set2)  #Join set1 and set2, but keep only the duplicates:
    set3 = set1.difference(set2)  #Keep all items from set1 that are not in set2:
    set3 = set1.symmetric_difference(set2)  #Keep the items that are not present in both sets:
    print(set3)

#Python Dictionaries:

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = thisdict["model"]  #Access dictionary items
    x = thisdict.get("model")

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["year"] = 2018  #Change items
    thisdict.update({"year": 2020})

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["color"] = "red"  #Add items
    print(thisdict)

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.pop("model")  #Remove items
    print(thisdict)

    for x in thisdict:
        print(thisdict[x])  #Print all values in the dictionary, one by one:
    for x in thisdict.values():  #use the values() method to return values of a dictionary:
        print(x)  
    for x in thisdict.keys():  #use the keys() method to return the keys of a dictionary:
        print(x)
    for x, y in thisdict.items():  #Loop through both keys and values, by using the items() method:
        print(x, y)

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    mydict = thisdict.copy()  #Make a copy of a dictionary with the copy() method:
    print(mydict)

    #Nested dictionaries
    child1 = {
        "name" : "Emil",
        "year" : 2004
    }
    child2 = {
        "name" : "Tobias",
        "year" : 2007
    }
    child3 = {
        "name" : "Linus",
        "year" : 2011
    }
    myfamily = {
        "child1" : child1,
        "child2" : child2,
        "child3" : child3
    }

a = 200  #Python if...else
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

i = 1  #Python while loops
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

adj = ["red", "big", "tasty"]  #Python for loops
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

