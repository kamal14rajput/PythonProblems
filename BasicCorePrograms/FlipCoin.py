import random

total_flips = int(input("How many times you want to flip coin:-"))
i = 1
tail = 0
while i <= total_flips:
    i += 1
    flip_coin = random.uniform(0, 1)
    if flip_coin < 0.5:
        print("It's Tails")
        tail += 1
    else:
        print("It's Heads")
percentage = (tail / total_flips) * 100
print("Percentage of Tails is: ", percentage, "%")
print("Percentage of Heads is: ", 100 - percentage, "%")
