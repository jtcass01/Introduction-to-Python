# Arbitrary Number of Arguments Example
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def make_sandwich(size, *toppings):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)