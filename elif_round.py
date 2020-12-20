income = int(input())
if (income <= 15527):
    percent = 0
    calculated_tax = 0

elif (15528 <= income <= 42707):
    percent = 15

elif (42708 <= income <= 132406): #elif income in range(42_708, 132_407):
    percent = 25

elif (132407 <= income):
    percent = 28

calculated_tax = round(income * percent * 0.01)
print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')