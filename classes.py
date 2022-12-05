"""
Classes / Objects: A class is like an object constructor, or a blueprint for
                   creating objects. An object has properties and methods
"""

""" Object Oriented Programming represents a way of organizing a program using classes and objects """


# Create a Class: We can use  the class of Person as a blueprint to create as many
# instances as we want of it that we call objects
class MyClass:
    x = 10
    y = 100


# create an Object
my_object = MyClass()
print(my_object.x)
print(my_object.y)


# The __init__() Function: is used to initialise the object
class Person:
    # The self parameter is the reference to the current instance of the class
    # and is used to access variables that belong to the class
    def __init__(self, firstname, lastname, age):   # Special method
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


person1 = Person("Arouna", "Mounchili", 26)
print(person1.firstname, person1.lastname, person1.age)

print(person1)


# The __str__() Function: controls what should be returned when the class
# objet is represented as a string
class Person:
    # The init method is called when an instance of the class is created
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.lastname} {self.firstname} is {self.age} years old.\n"


person1 = Person("Arouna", "Mounchili", 26)
print(person1)


# object Methods: Methods are functions that belong to the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


person1 = Person("Raoul", 24)
print(person1.name)
print(person1.age)
person1.change_name("Henry")
person1.set_age(19)
print(person1.name)
print(person1.age, "\n")

# Modify object properties
person1.name = "Ismael"
print(person1.name)

# Delete object properties
del person1.name
# print(person1.name)  #Error ('Person' object has no attribute 'name')

# Delete Object
del person1
