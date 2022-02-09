year = int(input("Enter the year: "))
if 999 < year < 10000:
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print("Please enter 4 digit number.")
