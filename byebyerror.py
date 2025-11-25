valid = False
try:
    n = int(input("please input a number"))
    while n%2==0:
        print("bye")
    valid = True
except ValueError:
    print("invalid number")