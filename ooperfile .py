with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print("words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()