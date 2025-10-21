print("do any command 1-10 to this list")
list =['a', 'b', 'c', 'd']
say = input("enter command:\nfirst,\n last, \n pop \n length, \n remove, \n sort, \n add, \n multiply, \n slice, \n reverse, \n clear")
if say == 'length':
    print("length :", len(list))
elif say == 'first':
    print("first :", list[0])
elif say == 'last':
    print("last :", list[-1])
elif say == 'add':
    answ = input("what letter?")
    list.append(answ)
    print("new :", list)
elif say == 'remove':
    noadd = input("what letter?")
    list.append(noadd)
    list.remove(noadd)
    print("update : ", list)
    answ = input("what letter?")
elif say == 'sort':
    list.sort()
    print("sorted:", list)
elif say == 'pop':
    list.pop(2)
    print("update:", list)
elif say == 'reverse':
    list.reverse
    print("reverse:", list)
elif say == 'multiply':
    print("multiply:", list*2)
elif say == 'slice':
    list = list[:2]
    print("sliced list:", list)
elif say == 'clear':
    list.clear()
    print("clear:",list)