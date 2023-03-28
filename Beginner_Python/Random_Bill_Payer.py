# Import the "random" module to generate a random integer
import random

# Ask the user to input a list of names separated by commas
names_string = input("Give me everybody's names, separated by a comma, \n")

# Split the input string into a list of individual names
names = names_string.split(", ")

# Generate a random integer between 0 and the length of the "names" list minus 1
index_random = random.randint(0, len(names) - 1)

# Print a message indicating which person will pay the bill
print(f'{names[index_random]} is going to pay for the bill today')
