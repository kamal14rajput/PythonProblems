import math

#user input x and y
x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

#Euclidean distance formula
distance = math.sqrt(x*x + y*y)

print("distance from (",x ,",",y ,") to (0, 0) = ", distance)
