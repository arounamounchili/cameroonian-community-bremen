"""
Python Loops: Repeat an action several times
"""

""" For Loops: A for loop is used for iterating over a sequence (lists, tuple, set, or string """

fruits = ["banana", "orange", 'apple', "ananas"]
for f in fruits:
    print(f)

# Looping through a String
name = "Elon Musk"
for n in name:
    print(n)

print()

# The break Statement
fruits = ["banana", "orange", 'apple', "ananas"]
for i in fruits:
    if i == "apple":
        break
    print(i)


print()
# The continue Statement
fruits = ["banana", "orange", 'apple', "ananas"]
for i in fruits:
    if i == "apple":
        continue
    print(i)


# The range() Function
for x in range(10):
    print(x)
print()

for x in range(3, 10):
    print(x)
print()

for x in range(0, 10, 2):
    print(x)
print()

# Nested Loops
x_position = [1, 2, 3, 4, 5]
y_position = [6, 7, 8, 9, 10]
for x in x_position:
    for y in y_position:
        print(x, y)


""" While Loops """

i = 0
while i < 5:
    print(i)
    i = i + 1

