"""
Lists: Lists are used to store multiple items in a single variable.
       Lists are ordered, changeable, and allow duplicates values.
"""

first = "Arouna"
second = "Ronald"
third = "Carlos"
fourth = "Freddy"

students = ["Arouna", "Ronald", "Carlos", "Freddy"]
print(students)
print()

# get the first element
students = ["Arouna", "Ronald", "Carlos", "Freddy"]
# indices:     0         1         2          3
print(students[0])
print()

# changes the value of an element in the list
students[0] = "Mounchili"   # get the first element
students[1] = "Samuel"      # get the second element
students[2] = "Diane"
students[3] = "Sandra"
print(students)
print()

# add a new element in the list
students.append("Carolle")
print(students)
print()


# List can contain different types of variables
number_of_people_in_classroom = [45, 67, "fifty", "twenty", 70]

# Slicing
ages = [10, 28, 35, 14, 45, 16, 7, 38]
print(ages[0:5])    # [10, 28, 35, 14, 45]
print(ages[2:5])    # [35, 14, 45]
print(ages[0::2])   # [10, 35, 45, 7]
print(ages[:5])     # [10, 28, 35, 14, 45]
print()

# List concatenation
my_list1 = ["a", "b", "c"]
my_list2 = ["d", "e", "f"]
my_list = my_list1 + my_list2
print(my_list)      # ['a', 'b', 'c', 'd', 'e', 'f']
print()

""" String """
my_string = "Hello!"
# my_string[1] = "a"  # not allowed because string are immutable


""" List methods """

# len() : get the length os a list
my_string = ["h", "e", "l", "l", "o"]
print(len(my_list))
print()

# append() : add an element to a list
my_string = ["h", "e", "l", "l", "o"]
my_list.append(",")
my_list.append("World")
print(my_list)

# insert() : add elements at specific indexes in a list
my_list = [1, 2, 3]
my_list.insert(2, 4)
print(my_list)

# pop() : delete elements from a list (remove the last element in the list
my_list = [1, 2, 3]
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)

# pop()
my_list = [1, 2, 3]
my_list.pop(1)  # delete the element at index 0
print(my_list)

# del
my_list = [1, 2, 3]
del my_list[0]
print(my_list)

# remove()
my_list = [1, 2, 3]
my_list.remove(3)
print(my_list)

# reverse() : reverse the elements in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.reverse()
print(my_list)      # [9, 8, 7, 6, 5, 4, 3, 2, 1]


""" Loop through a List """
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in my_list:
    # print(number)
    pass

for i in range(len(my_list)):
    # print(my_list[i])
    pass

""" List comprehension """
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [print(x) for x in my_list]
