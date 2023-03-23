# Initialize a variable to store the sum of even numbers
sum_even = 0

# Loop through numbers 1 to 100
for number in range(1, 101):
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the sum variable
        sum_even += number

# Print the sum of all even numbers
print(sum_even)
# Loop through numbers 1 to 100
for num in range(1, 101):
    # Check if the number is not divisible by 3 or 5
    if num % 3 != 0 and num % 5 != 0:
        # Print the number
        print(num)
    # Check if the number is divisible by 3 and not by 5
    elif num % 3 == 0 and num % 5 != 0:
        # Print "Fizz"
        print('Fizz')
    # Check if the number is divisible by 5 and not by 3
    elif num % 5 == 0 and num % 3 != 0:
        # Print "Buzz"
        print('Buzz')
    # Check if the number is divisible by both 3 and 5
    elif num % 3 == 0 and num % 5 == 0:
        # Print "FizzBuzz"
        print('FizzBuzz')
