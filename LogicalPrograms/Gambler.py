import random

#input from user
stake = input("Enter number of stake gambler has:")
goal = input("Enter gamblers goal:")
numOfTimes = input("Enter number of times he wants to play:")

#initializing
bets = 0
wins = 0

for i in numOfTimes:
    totalMoney = int(stake)
    while 0 < totalMoney < int(goal):
        bets += 1
        if random.randint(0, 1) < 0.5:
            totalMoney += 1
            wins += 1
        else:
            totalMoney -= 1


    print(int(wins), int(numOfTimes))
    percentage = (int(wins) / int(numOfTimes)) * int(100.0)
    print("Percent of games won = ", percentage)
    print("Percent of games loss = ", 100 - percentage)
    print("Avg bets = ", int(1.0) * int(bets) / int(numOfTimes))