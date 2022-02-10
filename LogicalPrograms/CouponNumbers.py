import random

def generateCoupon(totalChars, coupon, luckycode):
    if totalChars <= 0:
        print("Invalid Input")
    else:
        print("Random coupon code is:")
        code: str = ''
        for i in range(0, totalChars):
            slice_start = random.randint(0, len(luckycode) - 1)
            code += luckycode[slice_start: slice_start + 1]

    if len(coupon) == totalChars:
        if coupon == code:
            print("Random coupon is:", code)
            print("User coupon is: ", coupon)
            print("You won!!!")
        else:
            print("You lost!Try again.")


#user inputs
totalChars = int(input("Enter the length of the coupon:"))
coupon = input("Enter the coupon number:")
luckycode = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

generateCoupon(totalChars, coupon, luckycode)