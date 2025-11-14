def fibonacci():
    f1 = 0
    f2 = 1
    i = 0
    print(f1,f2)
    while(i<10):
        f3 = f1 + f2
        print(f3,end=" ")
        f1 = f2
        f2 = f3
        i = i+1
fibonacci()