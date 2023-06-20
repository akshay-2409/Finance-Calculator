import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")


option = input()
#user will enter either option. If none of them are selected, they will get a message saying Invalid selection!

'''
deposit and invest_interest_rate variables are inputted as a float to ensure the user can add decimal values
interest_rate variable is then divided by 100 after the input has been made so inorder for the calculation to be correct
The function round() will round the decimal to the given number stated, in this case it is set to 2
'''

if option == 'investment' or option == 'INVESTMENT' or option == 'Investment':
    deposit = float(input("How much will you deposit? "))
    invest_interest_rate = float(input("Enter the interest rate: "))
    years_invest = int(input("How many years do you plan to invest? "))
    interest_rate = invest_interest_rate/100
    
    interest = input("Enter type of interest; simple or compound: ")
    if interest == "simple":
        interest_total = deposit *(1 + interest_rate*years_invest)

    elif interest == "compound":
        interest_total = deposit * math.pow((1+interest_rate), years_invest)

    else:
        print("Invalid interest selection!")
    print("The total", interest, "interest amount after" , years_invest, "years is", round(interest_total,2))

elif option == 'bond' or option == 'BOND' or option == "Bond":
    house_value = float(input("Enter current house value: "))
    bond_interest_rate= float(input("Enter the yearly interest rate: "))
    months_repayment = int(input("How many months do you plan to repay the bond? "))
    monthly_interest_rate = (bond_interest_rate/100) / 12
    repayment = (monthly_interest_rate * house_value)/(1 - (1 + monthly_interest_rate)**(-months_repayment))
    
    print("The total monthly", option, "repayments is ", round(repayment,2))

else: 
    print("Invalid selection!")