import math
#taking input from user
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

#calculating equation
delta = (b*b) - (4*a*c)
delta2 = math.sqrt(abs(delta))
if(delta > 0):
    x1 = (-b + delta2)/(2*a)
    x2 = (-b - delta2)/(2*a)
    print("Roots are : " , x1 , " and ", x2);

elif(delta == 0):
    print("Root is : " , (-b)/(2*a))
else:
    print("Roots are not real.")
