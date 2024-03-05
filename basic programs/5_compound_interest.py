
def compound_interest(principal, rate, time):

    amount = principal * (pow((1 + rate / 100), time))
    compound_interest = amount - principal
    return compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

interest = compound_interest(principal, rate, time)

print("Compound Interest =", round(interest, 2))