# Ask the user to enter their height and weight
height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))

# Calculate the BMI by dividing weight by height squared
BMI = weight / (height ** 2)

# Round the BMI to 3 decimal places
BMI_Final = float("{:.3f}".format(BMI))

# Print the final BMI value
print(BMI_Final)

# Check the BMI category and print an appropriate message
if BMI_Final < 18.5:
    print("You are UnderWeight")
elif BMI_Final > 18.5 and BMI_Final < 25:
    print("Normal Weight")
elif BMI_Final > 25 and BMI_Final < 30:
    print("Over Weight")
elif BMI_Final > 30 and BMI_Final < 35:
    print("Obese")
else:
    print("Clinically Obese")
