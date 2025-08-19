"""
List Comprehension can be used for
List, Range, String and Tuple -(ordered data structures)
"""
# Format without condition
# new_list = [ new_item for item in old_list ]

old_list = [1, 2, 3]
new_list = [ i * 2 for i in old_list ]
print(old_list)
print(new_list)

print()

language = "Python"
letter = [letter for letter in language]
print(letter)