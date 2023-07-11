import random as r
p = 0
w = 0
t = 0

print("Welcome to rock, paper scissors, enter 1 to start")
s = int(input("Enter Here: "))

while s == 1:
    num = r.randint(1, 3)
    print("")
    print("Enter 1 to choose rock")
    print("Enter 2 to choose paper")
    print("Enter 3 to choose scissors")
    rps = int(input("Enter Here: "))
    print("")
    t = t + 1
    while rps < 1 or rps > 3:
        print("Please only enter values from 1 to 3 inclusive")
        print("Enter 1 to choose rock")
        print("Enter 2 to choose paper")
        print("Enter 3 to choose scissors")
        rps = int(input("Enter Here: "))
        print("")
    if num == rps:
        print("It was a tie")
        if num == 1:
            print("The computer chose rock too")
        if num == 2:
            print("The computer chose paper too")
        if num == 3:
            print("The computer chose scissors too")
    if num == 1 and rps == 2:
        print("You win! The computer chose rock")
        p = p + 1
    if num == 2 and rps == 3:
        print("You win! The computer chose paper")
        p = p + 1
    if num == 3 and rps == 1:
        print("You win! The computer chose scissors")
        p = p + 1
    if num == 2 and rps == 1:
        print("You lost. The computer chose paper")
    if num == 3 and rps == 2:
        print("You lost. The computer chose scissors")
    if num == 1 and rps == 3:
        print("You lost. The computer chose rock")
    w = (p / t) * 100
    print("")
    print("Thank you for playing!, enter 1 to start again, enter any other number to stop")
    s = int(input("Enter Here: "))

print("")
print("Your total number of rounds are: ", t)
print("Your total number of rounds won are: ", p)
print("Your win-rate is: ", w), "%"
