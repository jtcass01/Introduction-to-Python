message=input("Tell me your name: ")
print("Hello, " + message + "!")

age = input("How old are you? ")
print("age", age)
age = int(age)     # Cast age to an integer
new_age = age - 1
print("new_age", new_age)


height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
