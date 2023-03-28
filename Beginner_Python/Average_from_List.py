# Initialize the sum variable to 0
sum = 0

# Ask the user to input a list of student heights, separated by commas
student_heights = input('Input a list of student heights: ').split(', ')

# Loop through each element in the student_heights list and convert it to an integer
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
    # Add the integer value to the sum variable
    sum += student_heights[n]

# Calculate the average height of the students and round it to the nearest integer
average = round(sum / len(student_heights), 0)

# Print the list of student heights and the average height
print(f'students heights:  {student_heights}\nAverage is:  {average}')
