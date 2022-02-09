#user input
N = int(input("Enter the number:"))

if N > 1:     #only positive integer
    i = 2
    print("prime factors of", N ,"are: ")
    while i <= N:
        while(N % i == 0):
            print(i)
            N = N/i;
        i +=1
else:
    print("Please enter number greater than 1!")