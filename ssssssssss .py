num = 2

flag = False
if num > 1:
    for i in range (2,num):
        if (num % i):
            flag = True
            break
if flag:print(num ,"is not a prime number")
else:
    print(num,"it is a prime number.")