print("Welcome to the tip Calculator.\n")
total_bill = float(input('What was the total bill? $'))
tip_amount = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
new_total_bill = ((tip_amount / 100) * total_bill) + total_bill
numOfPeople = int(input("How many people to split the bill? "))
# amount_payable = round(new_total_bill / numOfPeople, 2)
amount_payable = "{:.2f}".format(new_total_bill / numOfPeople)
print(f"Each person should pay: ${amount_payable}")
