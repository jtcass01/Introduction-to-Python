# Class Example 1
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Constructor; Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

def describe_dog(dog):
    print("dog's name is " + dog.name.title() + ".")   # Access the dog's name.
    print("dog is " + str(dog.age) + " years old.\n")  # Access the dog's age.

if __name__ == "__main__":  
    # Creating a class object; accessing attributes.
    my_dog = Dog('Michio', 1)                              # Construct a dog object.
    sophias_dog = Dog('crystal', 6)
    hannahs_dog = Dog('Cupcake', 0)
    samuels_dog = Dog('white rice', 0.5)
    alexs_dog = Dog('dinner', 19)
    thomass_dog = Dog('butter', 10)

    describe_dog(my_dog)
    describe_dog(sophias_dog)
    describe_dog(hannahs_dog)
    describe_dog(samuels_dog)
    describe_dog(alexs_dog)
    describe_dog(thomass_dog)

    sophias_dog.sit()
    sophias_dog.roll_over()

    my_dog.sit()
    my_dog.roll_over()
