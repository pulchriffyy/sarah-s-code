number = 1634
instr = str(number)
product = (int(instr[0]))**4+(int(instr[1]))**4+(int(instr[2]))**4+(int(instr[3]))**4
if product == number:
    print(product,"is a armstrong number")
else:
    print(product,"is not a armstron number")