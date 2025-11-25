try:
    n = int(input("Please enter a number:  \n "))
    print("The number entered is: ",n)
except ValueError as ex:
        print("exception: enter a valid number.")