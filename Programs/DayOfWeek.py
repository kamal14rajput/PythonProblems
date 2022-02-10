day = int(input("Enter the day:"))
month = int(input("Enter the month:"))
year = int(input("Enter the year:"))

if 1 <= day <= 31 and 1 <= month <= 12:
    y = int(year - (14 - month) / 12)
    x = int(y + y / 4 - y / 100 + y / 400)
    m = int(month + 12 * ((14 - month) / 12) - 2)
    d = int((day + x + 31 * m / 12) % 7)

    if d == 0:
        print("You just Entered ",(d+1),"st day of week i.e  Sunday")
    elif d == 1:
        print("You just Entered ", (d + 1), "nd day of week i.e  Monday")
    elif d == 2:
        print("You just Entered ", (d + 1), "rd day of week i.e  Tuesday")
    elif d == 3:
        print("You just Entered ", (d + 1), "th day of week i.e  Wednesday")
    elif d == 4:
        print("You just Entered ", (d + 1), "th day of week i.e  Thursday")
    elif d == 5:
        print("You just Entered ", (d + 1), "th day of week i.e  Firday")
    elif d == 6:
        print("You just Entered ", (d + 1), "th day of week i.e  saturday")
    else:
        print("Something wrong happen!!!")
else:
    print("Please enter valid date.")