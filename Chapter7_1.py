message=input("Tell me your name: ")
print("Hello, " + message + "!")

age = input("How old are you? ")
print("age", age)
age = int(age)     # Cast age to an integer
new_age = age - 1
print("new_age", new_age)


height = input("How tall are you, in inches? ")
weight = input("How much do you weight, in lbs.? ")
height = int(height)
weight = int(weight)
if height >= 36 and weight <= 200:
    print("\nYou're tall and light enough to ride!")
elif height >= 36 and weight > 200:
    print("\nSorry, you are tall enough but you are too heavy.")
elif height > 112:
    print("\nHow's the weather up there? You can't ride!")
else:
    print("\nMaybe next time!")
