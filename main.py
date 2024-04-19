# Create the adding_practice list with the following entry: 273.15

adding_practice = [273.15]

# Use the append method to add the number 42 and the string "hello" to the list. Add these new items one at a time.  Print the list after each step to confirm the changes.

adding_practice.append(42)
print(adding_practice)

adding_practice.append("hello")
print(adding_practice)

# Use list concatenation to add these three items to the list all at once: [False, -4.6, '87'].

adding_practice += [False, -4.6, '87']

# Use the cargo_hold list for the next set of exercises.

cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

# Use bracket notation to replace 'slinky' in the list with 'space tether'. Print the list to confirm the change.

cargo_hold[5] = 'space tether'
print(cargo_hold)

# Remove the last item from the list with pop. Print the element removed and the updated list.

last_item = (cargo_hold.pop())
print(cargo_hold)
print(last_item)


# Remove the first item from the list with pop. Print the element removed and the updated list.

first_item = (cargo_hold.pop(0))
print(cargo_hold)
print(first_item)

# append and insert require arguments inside the (). Add the items 1138 and ‘20 meters’ to the the list - the number at the start and the string at the end. Print the updated list to confirm the changes.

cargo_hold.append('20 meters')
cargo_hold.insert(0,1138)
print(cargo_hold)

# Use the remove method to take the parrot out of cargo_hold, then print the updated list.

cargo_hold.remove('parrot')
print(cargo_hold)

# Use .format() to print the final list and its length. "The list ___ contains ___ items."

print("The list {0} contains {1} items.".format(cargo_hold, len(cargo_hold)))

# Use slices to make the following changes to the cargo_hold list. Be sure to print the list after each step to confirm your work.
cargo_hold = [1138, 'space suits', 'parrot', 'instruction manual', 'meal packs', 'space tether', '20 meters']

# Insert the string 'keys' at index 3 without replacing any other entries.

cargo_hold.insert(3, 'keys')
print(cargo_hold)

# Remove 'instruction manual' from the list. (Hint: The index method is helpful to avoid manually counting an index).

cargo_hold.remove('instruction manual')
print(cargo_hold)

# Replace the elements at indexes 2 - 4 with the items 'cat', 'book', and 'string cheese'.

cargo_hold[2:5] = ['cat', 'book', 'string cheese']
print(cargo_hold)

# Some methods—like append and pop—alter the original list, while others do not. Use the lists supplies_1 and supplies_2 to see if taking a slice or using the ``reverse`` and ``sort`` methods changes the original list.
supplies_1 = ['duct tape', 'gum', 3.14, False, 6.022e23]
supplies_2 = ['orange drink', 'nerf toys', 'camera', '42', 'Rutabaga']

# Print a slice of the last 3 items from supplies_1. Does slice alter the original list? Verify this by printing supplies_1 after taking the slice.

print(supplies_1[-3:])
print(supplies_1)


# reverse the first list, sort the second, and then print both lists. What is the difference between the two methods? Do reverse or sort alter the original lists?

supplies_1.reverse()
supplies_2.sort()

print(supplies_1)
print(supplies_2)

phrase = 'In space, no one can hear you code.'
my_list = ['B', 'n', 'n', '5']
cargo_hold = "water,space suits,food,plasma sword,batteries"

# The split and list methods convert a string into a list, while the join method does the opposite.

# See what happens when you print phrase.split() vs. phrase.split('e') vs. list(phrase). What is the purpose of the argument inside the ()?

print(phrase.split())
print(phrase.split('e'))
print(list(phrase))

# See what happens when you print ''.join(my_list) vs. 'a'.join(my_list) vs. '_'.join(my_list). What is the purpose of the argument inside the ()?

print(''.join(my_list))
print('a'.join(my_list))
print('_'.join(my_list))

# Split the cargo_hold string at each comma, alphabetize the list with sort, then combine the elements into a new string. Use a hyphen to join the elements together in the string.

cargo_hold_list = cargo_hold.split(',')
cargo_hold_list.sort()
new_string = '-'.join(cargo_hold_list)
print(new_string)

# Do split, list, or join change the original string/list?


# Lists can hold different data types, even other lists! A multi-dimensional list is one with entries that are also lists.

# Define and assign the element_1, element_2, and element_26 lists as specified in the instructions.

element_1 = ['hydrogen', 'H', 1.008]
element_2 = ['helium', 'He', 4.003]
element_26 = ['iron', 'Fe', 55.85]

# Use the append method to add each of the element lists to 'table'. Print table to see its structure.
table = []

table.append(element_1)
table.append(element_2)
table.append(element_26)
print(table)

# Use bracket notation to examine the difference between printing table[1] and table[1][1]. Describe the difference out loud. Go ahead, talk to your screen.

print(table[1])
print(table[1][1])


# Using bracket notation and the table list, print the mass from element_1, the name from element_2 and the symbol from element_26.

print(table[0][2])
print(table[1][0])
print(table[2][1])

# table is an example of a 2-dimensional list. The first “level” contains the element lists, and the second level holds the name/symbol/mass values. Experiment! Create a 3-dimensional list and print out one entry from each level in the list.
table_3d = []
table_3d.append(table)
table_3d.append(table) 
table_3d.append(table)
print(table_3d)
print(table_3d[0][2][1])
print(table_3d[2][1][1])
