print("Welcome to the tip calculator")
total = float(input("What was the total bill?\n $"))
percentage = int(input("What percantage tip would you like to give? 10, 12, or 15? \n: "))
people = int(input("How many people to split the bill?\n: "))

if percentage == 10:
	answer = (total / people) * 1.10

elif percentage == 12:
	answer = (total / people) * 1.12

elif percentage == 15:
	answer = (total / people) * 1.15

else:
	print("ERROR!!! Try Again!")

print("Your total is: $%.2f" %answer)