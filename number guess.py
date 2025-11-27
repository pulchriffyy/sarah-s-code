import random
while True:
          r = random.randint(1,10)
          i = int(input("Enter a number to guess the correct one! 1-10"))
          if i == r:
                    print("you won! you guessed it! pc:",r,"you:",i)
          else:
                    print(" pc:",r,"you:",i)
          o = input("continue? (y/n)")
          if o!="y":
                  break