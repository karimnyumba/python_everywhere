# Ask the user to input a two-digit number
two_digit_num = input("Type a two digit number: ")

# Convert the input to a string
new_two_digit_num = str(two_digit_num)

# Extract the first digit as an integer
first_digit = int(new_two_digit_num[0])

# Extract the second digit as an integer
second_digit = int(new_two_digit_num[-1])

# Add the two digits together and print the result
print(first_digit + second_digit)
