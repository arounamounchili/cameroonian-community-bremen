"""
Tuples: Tuples are collections that are ordered and unchangeable.
        Allows duplicate members.
"""

clothes = ("Shoes", "Jeans", "Short", "T-Shirt")
print(clothes)
print(len(clothes))
print(clothes[0:])
print(clothes.index('Jeans'))   # 1

# Membership Check: We can check whether an element is part of a tuple
# using 'in' and 'not in'
print('Shoes' in clothes)       # True
print('Shoes' not in clothes)   # False
