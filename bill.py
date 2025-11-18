import math
def tc(ba,tp):
    t = ba*(1+0.01*tp)
    #t=round(t,2)
    print(f"please pay the amount:: ${t}")
a=int(input("enter the bill amount: "))
tip = int(input("Now, please enter tip percentage: "))
tc(a,tip)