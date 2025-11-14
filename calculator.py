def add():
    y = int(input("enter a number: "))
    x = int(input("enter another number: "))
    print(y,"+",x,"=",y+x)
def sub():
    y = int(input("enter a number: "))
    x = int(input("enter another number: "))
    print(y,"-",x,"=",y-x)
def mul():
    y = int(input("enter a number: "))
    x = int(input("enter another number: "))
    print(y,"x",x,"=",y*x)
def div():
    y = int(input("enter a number: "))
    x = int(input("enter another number: "))
    print(y,"/",x,"=",y//x)
print("Please select the following operations, \n a. add, \n b. subtract \n c. multiply \n d. divide")
ask = input("choose either a, b , c , or d. (also please write lowercase,)")
if ask == 'a':
    add()
elif ask == 'b':
    sub()
elif ask == 'c':
    mul()
elif ask == 'd':
    div()
else:
    print("please retry and enter a valid input.")