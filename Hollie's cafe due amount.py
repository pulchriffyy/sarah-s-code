import random
r = random.randint(1,3)
p = 1000.0

print("\n \n \n \n \n \n \n ˗ˏˋ [ hello! welcome to Holly's resturant, what can we get you today?] ࿐ྂ  \n \n \n \n  ꒰⸝⸝ 1:[(banana shake ($35.75)/)2: (chocochip muffin($50.0)) 3:(water($1.50))] ꒱ \n; .\n")
q1 = int(input("\n ❏ ⇢ [1 - 2 - or -  3 or ?]"))
if q1 == r:
          print("  ◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢ \n Oopsie daisy! item sold out!\n   ◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢ \n ✩ Please try again")
elif q1 == 1:
        print("before we get started with the point payments, you have to know how much points you have! \n ✩  you have",p," points.")
        
        q2 = int(input("How many of these do you want?"))
        a = 35.75*q2
        if a>100:
                print("I'm sorry! but please give within range of your points :)")
        else:
                print("♡ please pay and give a specified amount of money wisely, the money you have to pay for is ",a)
                ask = float(input("Please type here! : "))

                if ask>= p or a>=p or a>=ask:
                        print("\n ♡ please pay within your points. \n try again please,")
                else:
                        pass
                print("♡ money spent: ", ask,"\n ♡ money left: ",p-ask,"\n ♡ Change: ",ask-a)
elif q1 == 2:
        print("before we get started with the point payments, you have to know how much points you have! \n ✩  you have",p," points.")
        
        q2 = int(input("How many of these do you want?"))
        a = 50.0*q2
        if a>1000:
                print("I'm sorry! but please give within range of your points :)")
        else:
                print("♡ please pay and give a specified amount of money wisely, the money you have to pay for is ",a)
                ask = float(input("Please type here! : "))

                if ask>= p or a>=p or a>=ask:
                        print("\n ♡ please pay within your points. \n try again please,")
                else:
                        pass
                print("♡ money spent: ", ask,"\n ♡ money left: ",p-ask,"\n ♡ Change: ",ask-a)
elif q1 == 3:
        print("before we get started with the point payments, you have to know how much points you have! \n ✩  you have",p," points.")
        
        q2 = int(input("How many of these do you want?"))
        a = 1.50*q2
        if a>1000:
                print("I'm sorry! but please give within range of your points :)")
        else:
                print("♡ please pay and give a specified amount of money wisely, the money you have to pay for is ",a)
                ask = float(input("Please type here! : "))

                if ask>= p or a>=p or a>=ask:
                        print("\n ♡ please pay within your points. \n try again please,")
                else:
                        pass
                print("♡ money spent: ", ask,"\n ♡ money left: ",p-ask,"\n ♡ Change: ",ask-a)
else:
        print("♡ please retry and input somehting valid! :)")
print("Thank you for buying from hollies!")