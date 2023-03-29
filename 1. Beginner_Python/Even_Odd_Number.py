# Ask the user to enter a number to check
number = int(input("Which number do you want to check: "))

# Check if the number is even or odd and print the appropriate message
if number % 2 == 0:
    print('This is an even number')
elif number % 2 == 1:
    print('This is an odd number')
else:
    print('Unknown number')
