"""
Tuples: Tuples are collections that are ordered and unchangeable.
        Allows duplicate members.
"""

clothes = ("Shoes", "Jeans", "Short", "T-Shirt", "Jeans")
print(clothes)

# get the length
print(len(clothes))

# Create a tuple with one item
my_tuple = ("item 1", )     # add a comma after the item to create a tuple with only one item
# print(type(my_tuple))
print(my_tuple)

# Membership Check: We can check whether an element is part of a tuple
# using 'in' and 'not in'
clothes = ("Shoes", "Jeans", "Short", "T-Shirt")
print('Shoes' in clothes)       # True
print('Shoes' not in clothes)   # False

# Access Tuple items
my_tuple = (12, "a", "b", True, 0.1)
print(my_tuple[4])

# Range of Indexes
my_tuple = (12, "a", "b", True, 0.1, "e")
print(my_tuple[0:])
print(my_tuple[2:4])
print(my_tuple.index('b'))  # index = 2
print()

# Unpacking a Tuple
colors = ("green", "red", "yellow")
(green, red, yellow) = colors
print(green)
print(red)
print(yellow)
