import random
while True:
    ua = input("Hello and welcome to RPS!! choose:  rock - paper or - scissors? ")
    pa = ["rock","paper","scissors"]
    r = random.choice(pa)
    print(" \n You chose ... ",ua,"and computer chose",r,"!")
    if ua == r:
        print(" \n and you both are tied!")
    elif ua == "rock" and r == "paper":
        print("\n and..! computer has won!")
    elif ua == "paper" and r == "rock":
        print("\n and..! you win!!")
    elif ua == "rock" and r == "scissors":
        print("\n And...! you win")
    elif ua == "scissors" and r == "rock":
        print("\n and..! computer has won! ")
    elif ua == "paper" and r == "scissors":
       print("\n and..! computer has won! ")
    elif ua == "scissors" and r == "paper":
        print("\n and..! you have won!! ")
    d = input("Do you want to play again? (y/n):  ")
    if d!="y":
        break