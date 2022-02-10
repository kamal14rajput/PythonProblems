N = int(input("Enter the Nth harmonic number"))  #nth harmonic number

harmonic_number = 0
if N > 0:
    i = 1
    while i <= N:
        harmonic_number = harmonic_number + (1/i)
        i += 1
    print("The ", N,"th harmonic value is: ", harmonic_number)
else:
    print("Please enter number greater than 0 only!!!")
