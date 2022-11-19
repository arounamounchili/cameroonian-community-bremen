"""
String
"""

school_name = "University of Colorado"
name = 'Arouna'
greeting = "Hello students. I'm your professor!"
greeting = 'Hello students. I\'m your professor!'
print("\n")     # new line
print(greeting)
two_lines = "This is the first line \n and this is a second line"
print(two_lines)

# Multiline String
paragraph = """This is a first sentence that is written in this line.
The second sentence begin  here, and it is followed by a comma.
The last line is the line that close the paragraph."""
print(paragraph)
print()
paragraph = '''This is a first sentence that is written in this line.
The second sentence begin  here, and it is followed by a comma.
The last line is the line that close the paragraph.'''
print(paragraph)
print("\n")


"""
String operators
"""

# concatenate strings using the + operator
first_string = "First"
second_string = "Second"

concatenated_string = first_string + " " + second_string
print(concatenated_string)

repeated_string = first_string * 5
print(repeated_string)


""" String built-in methods """

# len() : is a method use to get a length of a string
my_name = "Mounchili"
print("The length of my name is: ", len(my_name))

# lower() : converts all characters of a string into lower case
my_name = "AROUNA"
print(my_name.lower())

# upper() : converts all characters of a string into uper case
greeting = "hello"
print(greeting.upper())

# replace() : is a method to replace a character or a substring of a string
# with another character or substring
greeting = "Hello"
modified_greeting = greeting.replace("e", "a")
print(modified_greeting)    # Hallo

# strip() : removes white spaces that can be in the beginning or the end of a string
greeting = " Hello   "
print(greeting.strip())

# split() : convert a string into an array of substrings based on a specific
# pattern that is mentioned as the separator
sentence = "We can use the split method to split this sentence in an array"
print(sentence.split(" "))

# join() : return a string from a given array
sentence_arrays = ['We', 'can', 'use', 'the', 'join', 'method']
print(" ".join(sentence_arrays))
print()


""" String formatting """

#
user = "Arouna"
greeting = "Hello, " + user
print(greeting)

# format()
greeting = "Hello, {}. Welcome to the Python programming course".format(user)
print(greeting)

greeting = "Hello, {0}. Welcome to the {1} course".format(user, "C/C++")
print(greeting)

name = "Mounchili"
today = "Saturday"
greeting = f'Good evening {name}. Today is {today}!'
print(greeting)
