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

# Using the range() function
print("\nUsing the range() function example")
for samuels_value in range(1, 5):
    print(samuels_value)
