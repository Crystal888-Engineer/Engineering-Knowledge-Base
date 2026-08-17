# Python Data Classes

# Standalone Fuctions: print(), type(), input()
# Methods of Class: upper(), replace(), lower()
# Operations: + / > < ==

# ***************** FUCTIONS *********************
# function_name(value)
# print('Hello')
# type(50)

# ***************** METHODS **********************
# value.method_name()

# print('hello'.upper())
# print(50.bit_length())

# **************** EXAMPLES ********************

text = "hi"  # String
number = 10  # Integer

print(type(text))  # Function
print(type(number))  # Function

print(len(text))
# print(len(number)) # This will error as Int has not length

print(text.upper())  # Method = Upper Case
# print(number.upper()) # This will error as Int cant upper
# Method = Returns bit lengh as it works with Integers but no String, they are different classes
print(number.bit_length())
