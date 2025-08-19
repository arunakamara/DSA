"""
List Comprehension can be used for
List, Range, String and Tuple -(ordered data structures)
"""
# Format without condition
# new_list = [ new_item for item in list ]

old_list = [1, 2, 3]
new_list = [ i * 2 for i in old_list ]
print(old_list)
print(new_list)

print()

language = "Python"
letter = [letter for letter in language]
print(letter)

print()

# Format for list comprehension with condition
# new_list = [ new_item for item in list if condition ]
# new_list = [ new_item if condition else option for item in list]

lst = range(21) # List from 0 to 20
new_list = [ i for i in lst if i % 2 == 0] 
print(new_list) # prints out only even numbers

print()

# Replacing the condition with a function
sentence = "My name is Aruna Kamara"

def is_consonant(letter):
    return letter.lower() not in ['a', 'e', 'i', 'o', 'u']

new_sentence = [letter for letter in sentence if is_consonant(letter)]
print(new_sentence)

print()

# With else clause
prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [ num if num > 0 else 0 for num in prev_list ]
print(new_list)