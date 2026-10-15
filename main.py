# collection = single variable used to store multiple values
# List [] = ordered and changeable. duplicates okay
# Set {} = unordered and immutable add/remove okay but no duplicates
# Tuple () = ordered and unchangeable.duplicates okay faster

#List
fruits = ["apple", "banana", "cherry","mango"]
print("pineapple" in fruits)
print(dir(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits.append("orange")
print(fruits)

fruits.remove("orange")
print(fruits)
fruits.insert(0,"grapes")
print(fruits)
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index("apple"))
print(fruits.index("banana"))



fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)



#Set
fruits = {"apple", "banana", "cherry","mango"}  #No duplicates are allowed in set

fruits.add("orange")
print(fruits)

fruits.remove("orange")
print(fruits)
print(fruits.clear())

# Tuple

fruits = ("apple", "banana", "cherry","mango")
print(fruits)
print(len(fruits))

print(fruits.count("apple"))
print(fruits.count("banana"))
print(fruits.add("pineapple")) # we cant add in tuple
