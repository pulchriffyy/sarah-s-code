ask=input("Enter a  following operation :: [1: divide, 2: addition , 3: subtraction , 4: multiply]")
if ask == "1" or ask.lower() == "division":
    num1= int(input("Please enter a number."))
    num2= int(input("Please enter another number"))
    print(num1/num2)
elif ask == "2" or ask.lower() == "addition":
    num1= int(input("Please enter a number."))
    num2= int(input("Please enter another number"))
    print(num1+num2)
elif ask == "3" or ask.lower() =="subtraction":
    num1= int(input("Please enter a number."))
    num2= int(input("Please enter another number"))
    print(num1-num2)
elif ask == "4" or ask.lower() =="multiply":
    num1= int(input("Please enter a number."))
    num2= int(input("Please enter another number"))
    print(num1/num2)
else:
    print("Please  enter a valid keyword.")