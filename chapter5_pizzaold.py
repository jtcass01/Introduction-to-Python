# Example 1
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("")

# Example 2
requested_toppings = ['mushrooms', 'extra cheese']
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!\n")


# Example 3
available_toppings = ['mushrooms', 'olive','green peppers',
                      'pepperoni','pineapple', 'extra cheese']
requested_toppings = ['mushrooms','french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
