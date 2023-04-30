'''Chapter 4 notes related to Python Crash Course by Eric Matthes'''
# ~~~~ LIST SYNTAX ~~~~
# for VARIABLE in LIST:
#   Do something
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician + ", that was a great trick!")

    for character in magician:
        print(character)    
print("end")

# Using the range(START, STOP, INCREMENT=1) function
print("\nUsing the range() function example")
for samuels_value in range(1, 10):
    print(samuels_value)

print("")

# range() example 2
squares = []                # Initialize an empty list
for value in range(1, 11):  # Loop over the range 1-10 by 1
    square = value**2       # Square each value and store in 'square'
    squares.append(square)  # store 'square' in list 'squares'
print(squares)              # print the final list

print("")

# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Digits: " + str(digits))
minimum_value = min(digits)
print("minimum value: " + str(minimum_value))
maximium_value = max(digits)
print("maximium value: " + str(maximium_value))
total = sum(digits)
print("total: " + str(total))
