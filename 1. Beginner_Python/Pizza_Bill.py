# Initialize the bill to zero
bill = 0

# Display a welcome message to the user
print('Welcome to Python Pizza Deliveries')

# Prompt the user to enter the size of the pizza they want
size = input('What size pizza do you want? S, M, or L ')

# Prompt the user to indicate whether they want pepperoni or not
add_pepperoni = input('Do you want pepperoni? Y or N ')

# Prompt the user to indicate whether they want extra cheese or not
extra_cheese = input('Do you want extra cheese? Y or N')

# Determine the cost of the pizza based on the size and toppings
if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
elif size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
else:
    # The user entered an unknown size
    print('Unknown size of Pizza')

# Add the cost of extra cheese to the bill if the user requested it
if extra_cheese == 'Y':
    bill += 2

# Display the total bill to the user
print(f"Your bill is ${bill}")
