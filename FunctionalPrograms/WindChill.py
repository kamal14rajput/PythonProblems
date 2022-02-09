import math
#taking inputs
t = int(input("Enter the temperature:"))  #temperature
v = int(input("Enter the temperature:"))  #wind speed

if t < 50 and 120 > v > 3:
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print("Temperature = " , t)
    print("Wind speed  = " , v)
    print("Wind chill  = " , w)
else:
    print("Please enter valid values.")
