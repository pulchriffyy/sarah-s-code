for i in range(1,100):
    for j in range(2,i-1):
        if i%j==0:
            print(f"{i} Its not a prime number")
            break
    else:
        print(f"{i} is a prime number")