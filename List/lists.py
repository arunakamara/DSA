
shoppingList = ['Milk', 'Cheese', 'Butter']

# Accessing Element
print(f"First item: {shoppingList[0]}")
print(shoppingList[-1])
print(shoppingList[-2])
print(shoppingList[-3])

# Traverse
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]
    print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update - O(n)
myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

# append - O(1)
myList.append(55)

# extend - O(n)
newList = [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))


# Deleting an element from the List
print(myList)
# pop - O(1)
# print(myList.pop(-3))

# delete method 
# del myList # Deletes the entire list
del myList[-1]
del myList[2: 5]

# remove method
myList.remove(70)

print(myList)



