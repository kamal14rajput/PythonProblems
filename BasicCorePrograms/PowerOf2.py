N = int(input("Enter the value of N:-"))
if 0 <= N < 31:
    i = 1
    while i <= N:
        print("power of 2 is:-", 2 ** i)
        i += 1
else:
    print("Please enter number between 0 and 31")

