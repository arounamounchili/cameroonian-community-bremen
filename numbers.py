""" Numbers in Python: integers, floats, complex """


# Integers
number1 = -10
number2 = 12
result1 = -10 + 4 # 6
result1 = number1 + number2
print("The result is: ", result1)

# Floats
height = 63.459
weight = float(80) # 80.0
print("The weight is: ", weight)  # 80.0
print("")

x = 76.34e3   # e or E indicate the power of 10
print("x is: ", x)

# Complex numbers
complex_number1 = 3 + 6j
complex_number2 = 10 + 3j
print("\nThe complex number 1 is: ", complex_number1)
print("The complex number 2 is: ", complex_number2)
result2 = complex_number1 - complex_number2
print("The result of the subtraction of complex number is: ", result2)


# Verify the type of any objet in Python
print(type(weight))
print(type(result1))
print(type(result2))

# type conversion
a = 19      # int
b = 3.5     # float
c = 3j      # complex

x = float(a)    # convert from int to float
y = int(b)      # convert from float to int
z = complex(a)  # convert from int to complex
