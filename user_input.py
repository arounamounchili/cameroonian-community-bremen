"""
User Input
"""

# We are able to ask the user for input using the method input()
username = input("What is your username: ")
print("Your username is: " + username)

number = int(input("Enter a number: "))  # int("45")  => 45
factor = 4 * number
print(f'The addition of {number} * 4 is {factor}')