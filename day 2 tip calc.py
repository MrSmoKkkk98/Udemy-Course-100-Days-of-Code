# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
bill = input("""Welcome to the tip calculator?
What was the total bill?\n$""")
tip = input("What percantage tip would you like to give?\n")
person = input("How many people to split the bill?\n")
each_person_payment = (float(bill) / int(person)) * (1 + int(tip) / 100)
result = "{:.5f}".format(each_person_payment)
print(f'Each person should pay: ${result}')
