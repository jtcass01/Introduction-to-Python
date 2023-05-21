variable = 5
print(variable)

result = variable == 5
print(result)

result = variable == 4
print(result)

result = variable != 3
print(result)

result = variable < 10
print(result)

result = variable > 1
print(result)

result = 1 < variable < 6
print(result)

result = 1 < variable < 3
print(result)

result = (variable > 1) or (variable > 7)
print(result)

# Amusement park pricing example
age = 28
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 8
print("Your admission cost is $" + str(price) + ".")

# Amusement Park Example 2
age = 28
if age < 4 or age > 65:
    price = 0
elif age < 18:
    price = 5
else:
    price = 8
print("Your admission cost is $" + str(price) + ".")

