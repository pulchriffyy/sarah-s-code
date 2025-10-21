
def enjoyck():
    yorn=input("Hello and Welcome to calculator kingdom! would you like to get started?(y/n)")
    name= input(" enter your name here! :  ")
    print("Lovely name", name ,"!")
    if yorn == "y":
        num = int(input("Number "))
        num2 = int(input("Number "))
        print("number 1: ", num)
        print("Number 2: ", num2)
        print("add:", num + num2)
        print("difference:", num - num2)
        print("product:", num * num2)
        print("Division:", num / num2)
        print("Floor Division:", num // num2)
        print("modulus operation:", num % num2)
        print("Square:", num2 ** 2)
        print("Square Root:", num ** 0.5)
        print("Equal ??", num == num2)
        print("Number 1 greater?", num > num2)
        print("Number 2 greater?", num < num2)
        print("Not Equal ??", num != num2)

        result = num / 2 + num2 ** 2 + 10
        print("answer of given equation is:", result)
        
    else:
        print("please enter valid output! // we'll wait for you :)")
enjoyck()
yumyum = input("play again?")
if yumyum == "y" or yumyum == "yes":
    enjoyck()
elif yumyum == 'n' or yumyum =='no':
    print("I guess we'll see you again! good bye :)")
