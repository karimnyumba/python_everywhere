# Ask the user for their current age
age = int(input("What is your current age: "))

# Calculate how many years the user has left until they reach 90 years old
years_left = 90 - age

# Calculate how many days, weeks, and months the user has left
days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

# Print the results
print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
