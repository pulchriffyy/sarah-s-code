import random
def startt():
    rand = int(random.randint (1,10))
    num = int(input("enter a number to 1-10 and see if its correct."))
    if num == rand:
        print("correct!")
    elif num>10:
        print("out of range.")
    else:
        print("incorrect")
startt()