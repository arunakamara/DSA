myString = 'span'

myStrings = "span span span"
delimiter_string = "span-span-span"

# To convert to list
myList = list(myString)

print(myString)
print(myList)

# This splits the string by each character and make a list of it.
print(list(myStrings)) 

print()
# multiple words
delimiter_list = delimiter_string.split("-")
print(f"With delimiter: {delimiter_list}")
myLists = myStrings.split()
print(myStrings)
print(myLists)


# To convert to string
print("".join(myList))
print(" ".join(myLists))

