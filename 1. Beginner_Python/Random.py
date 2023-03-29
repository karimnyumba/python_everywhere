# Import the "random" module
import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)

# Print the random integer
print(f'{random_integer}')

# Generate a random float between 0 and 1
random_float = random.random()

# Generate a random float between 0 and 5 with three decimal places
random_greaterFloat = '{:.3}'.format(5 * (random.random()))

# Print the random floats
print(random_float, random_greaterFloat)
