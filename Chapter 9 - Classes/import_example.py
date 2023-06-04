# Import example
from car import Car
from dog import Dog, describe_dog

# Create an old car with a different default odometer reading
jacobs_car = Car('toyota', 'celica', 2000, 3000, initial_reading=230000)
print(jacobs_car.get_descriptive_name())

my_dog = Dog('Michio', 1)   # Construct a dog object.
describe_dog(my_dog)        # Describe the dog.