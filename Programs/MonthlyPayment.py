principal = int(input("Enter the principal:"))  # user input
year = int(input("Enter the year:"))
rate = int(input("Enter the rate percentage:"))


def monthlyPayment(principal, year, rate):
    n = 12 * year;
    r = rate / (12 * 100)
    payment = principal * r / 1 - (1 + r) ** (-n)
    print("Monthly Payment is ", payment)


monthlyPayment(principal, year, rate)           # function call
