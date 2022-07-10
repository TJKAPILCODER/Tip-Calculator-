
print("Welcome to the tip calculator!")
# ask for total bill
total_bill = input("What was the total bill? $")
# convert bill to float 
total_bill = float(total_bill)
# ask for percentage
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
# convert percentage to int
percentage = int(percentage)
# ask how many people splitting bill
people = input("How many people are splitting the bill? ")
# convert people to int
people = int(people)
# convert percentage to decimal
step1 = percentage / 100
# multiply total bill by decimal
step2 = total_bill * step1
# add new value to total bill to get new total
step3 = total_bill + step2
# divide new total by number of people
step4 = step3 / people
# round final to 2 decimal places 
step5 = round(step4, 2)
print(f"Each person should pay: ${step5}")