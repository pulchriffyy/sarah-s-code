import random

def start():
    rand = int(random.randint(1,10))
    print("Welcome to the..GUESSING GAME!")
    player = input("Enter your username.")
    wannaplay = input("Hi, {}!! would yo like to play the guessing game? (Enter y or n)".format(player))
    attempts = 0
    while wannaplay.lower() == "y":
        try:
            guess = int(input("pick a number (1-10)"))
            if int(guess) < 1 or int(guess)>10:
                raise ValueError("enter number within range 1-10.")
            if int(guess) == rand:
                print("Correct!")
                attempts += 1
                print("it took you {} attempts".format(attempts))
                playag = input("Play again? enter y/n")
                attempts = 0
                rand = input("random.randint(1,10)")
            if playag.lower == 'n':
                print("hope you enjoyed, have a splendid day! :) ")
                break
            elif int(guess) > rand:
                print("Oops! it's higher!")
                attempts += 1
        except ValueError as err:
            print("oof, invalid value dectected! try again. :o ")
            print("({}).format(err)")
    else:
        print("incorrect :C ")
if __name__ == '__main__':
    start()