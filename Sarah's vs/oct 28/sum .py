n = int(input("enter the value of n: "))
print("numbers from {0} to {1} are:".format(n,1))
for i in range(n,0,-1):
    print(i)

for i in range(1,100,2):
    print(i)
sum = 0 
for i in range(1,10):
    sum = sum +i
print("result of adding all integers of 10: ",sum)