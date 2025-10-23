while True:
    ask=input("Enter a  following operation :: [1: divide, 2: addition , 3: subtraction , 4: multiply , 5:square root 6: suprise]")
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
        print(num1*num2)

    elif ask == "5" or ask.lower() =="square root":
        num1= int(input("Please enter a number."))
        print(num1**0.5)

    elif ask == "6" or ask.lower() =="suprise":
        import random
        rand = int(random.randint (1,4))
        if rand == 1:
            rad = int(random.randint (1,100))
            ran = int(random.randint (1,100))
            print(rad,"+",ran,"=", rad+ran)

        elif rand == 2:
            rad = int(random.randint (1,100))
            ran = int(random.randint (1,100))
            print(rad,"-",ran,"=", rad-ran)
            
        elif rand == 3:
            rad = int(random.randint (1,100))
            ran = int(random.randint (1,100))
            print(rad,"/",ran,"=", rad/ran)
        elif rand == 4:
            rad = int(random.randint (1,100))
            ran = int(random.randint (1,100))
            print(rad,"*",ran,"=", rad*ran)
    else:
        print("Please  enter a valid keyword.")