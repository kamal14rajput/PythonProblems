c = int(input("Enter the non-negative number:"))

epsilon = 1e-15                     #relative error tolerance
t = c                               #estimate of the square root of c

#repeatedly apply Newton update step until desired precision is achieved
while (abs(t - c/t) > epsilon*t):
    t = (c/t + t) / 2.0

#print out the estimate of the square root of c
    print(t)