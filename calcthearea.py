def sq():
          a = float(input("enter the length of your square!   : "))
          b = float(input("enter the length of your square!   : "))
          print("the area of the given numebrs is:",a*b)
ask = input("do you want to calculate the area of a square? y/n")
if ask == "y":
        sq()
elif ask == 'n':
        print("okay see you next time!")
else:
        print("please enter a valid input. ")