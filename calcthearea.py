def sq():
          a = float(input("enter the length of your rectangle!   : "))
          b = float(input("enter the length of your rectangle!   : "))
          print("the area of the given numebrs is:",a*b)
ask = input("do you want to calculate the area of a rectangle? y/n")
if ask == "y":
        sq()
elif ask == 'n':
        print("okay see you next time!")
else:

        print("please enter a valid input. ")
