dollars = float(input("Enter your principal amount in dollars: "))
interest = float(input("Enter the interest rate as a percentage: "))
years = int(input("How many years will you store the money: "))
interestMade = ((dollars * interest) * years)/100
print(f"After {years} years you will have: {(interestMade + dollars).__round__(1)}")