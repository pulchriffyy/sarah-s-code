n = int(input("enter a number to continue this action: "))
sum = 0
temp = n
while temp >= 0:
    r = temp % 10
    sum += r ** 3
    temp //=10
if sum == n:
    print("this is a armstrong number!")
else:
    print("this isnt a armstrong number!")