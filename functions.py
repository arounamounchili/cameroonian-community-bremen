"""
Functions: A function is block of code that you can use over and over again,
           rather than writing it out multiple times. Functions enable programmers
           to break down or decompose a problem into smaller chunks, each of which
           performs a particular task.
"""

# Creating a Function
def my_function():
    print("This is our first function")
    print("This is our first function")


# Calling a function
my_function()


# Arguments: We can pass information into functions as arguments
def greeting(name):
    print(f'Hello, {name}')


def greeting2(name1, name2):
    print(f'Hello, {name1} and {name2}')


greeting("CCB")
greeting2("Jules", "Julie")
print()


# Arbitrary Arguments, *args: if the number of arguments is unknown,
# add a * before the parameter name
def get_last_name(*names):
    print("The first person is " + names[0])


get_last_name("Arouna", "Inteligencia", "Python")


# Keyword Arguments: we can also send arguments with the key = value syntax
# This way the order of the arguments does not matter
def greeting2(name1, name2):
    print(f'Hello, {name1} and {name2}')


greeting2(name2="Mounchili", name1="Arouna")
# greeting2("Arouna", "Mounchili")


# Arbitrary Keywords Arguments, **kwargs: if you do not know how many keyword
# arguments that will be passed into your function, add two asterisk: ** before
# the parameter name in the function definition
def get_name(**names):
    print("The first name is " + names["firstName"])


get_name(firstName="Arouna", LastName="Mounchili")
print()


# Default Parameter Value
def greeting(name="No name"):
    print("Hello, " + name)


greeting()
greeting("Ronald")


# Passing a List as an Argument
def show_list(my_list):
    for i in my_list:
        print(i)
    print()

a = show_list(["Arouna", "Ronald", "Carlos", "Freddy"])
print(a)
students = ["Arouna", "Ronald", "Carlos", "Freddy"]
show_list(students)


# Returns Values
def addition(number1, number2):
    return number1 + number2


a = 12
b = 8
result = addition(a, b)
print(f'The addition of a and b is: {result}\n')

""" 
Lambda Function: A lambda function is a small anonymous function that we can
                 use to return an output. Lambda functions are great way to 
                 make small, concise functions in Python.
"""

# Syntax: lambda arguments : expression
my_function = lambda a: a * 5
print(my_function(2))

#
my_function2 = lambda a, b: a - b
print(my_function2(5, 2))


# When to use Lambda functions: It can be used as an anonymous function inside
# another function
def my_function(value):
    return lambda x: x * value


the_double = my_function(2)
the_triple = my_function(3)
print(the_double(10))
print(the_triple(10))


def convert_to_euro(dollar):
    return dollar * 1.001


def convert_to_cent(euro):
    return euro * 100


def convert_to_km(meters):
    return meters / 1000


#
def conversion(operation, argument):
    return operation(argument)


dollar_to_euro = conversion(convert_to_euro, 10)
print(dollar_to_euro)
meters_to_km = conversion(convert_to_km, 1000)
print(meters_to_km)
print()


# Alternative

def conversion(operation, argument):
    return operation(argument)


dollar_to_euro = conversion(lambda dollar: dollar * 1.001, 10)
print(dollar_to_euro)