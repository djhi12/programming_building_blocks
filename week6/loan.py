from ssl import create_default_context
from turtle import down


print()

# Qualifying for a Loan
print("Rate from 1-10 \n")

loan_size = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("Hpw large is your down payment? "))

print()

decision = ""

# Condition for loan greater than or equal to 5
if loan_size >= 5:
    if credit and income >= 7:
        decision = "Yes"
    elif credit or income >= 7 and down_payment >= 5:
        decision = "Yes"
    elif credit and income != 7 and down_payment <= 4:
        decision = "No"


# Condition for loan less than to 5
if loan_size < 5:
    if credit < 4:
        decision = "No"
    elif credit >= 5 and income or down_payment >= 7:
        decision = "Yes"
    elif credit >= 5 and income and down_payment >= 4:
        decision = "Yes"
    else:
        decision = "No"

print(decision)

print()
