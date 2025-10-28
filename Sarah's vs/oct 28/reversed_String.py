st = input("enter a sentence or word: ")
s = ('')
for i in st:
    s = i + s
print("\n original line :: ", st)
print("reversed", s)