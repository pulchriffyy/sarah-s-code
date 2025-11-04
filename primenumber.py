l = int(input("Enter a lower number : "))
u = int(input("Enter a Higher number : "))
print("prime numbers between",l,"and",u,"is: ")
for num in range(l,u+1):
    if num > 1:
        for i in range(2,num-1):
            if num % i == 0:
                break
        else:
            print(num)