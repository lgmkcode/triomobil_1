alice = []
bob = []
ap = 0
bp = 0

alice.append(int(input("Enter the first number for Alice:")))
alice.append(int(input("Enter the second number for Alice:")))
alice.append(int(input("Enter the third number for Alice:")))
bob.append(int(input("Enter the first number for Bob:")))
bob.append(int(input("Enter the second number for Bob:")))
bob.append(int(input("Enter the third number for Bob:")))
print("Alice",alice)
print("Bob",bob)
   
if (100 >= alice[0] > bob[0] >= 1):
    ap += 1
    print("Number one. Alice receives 1 point.",ap,bp)
elif (1 <= alice[0] < bob[0] <= 100):
    bp += 1
    print("Number one. Bob receives 1 point.",ap,bp)
else:
    if ((100 >= alice[0] >=1 and 100 >= bob[0] >=1)):
        print("Number one. Values are equal.",ap,bp)
    else:
        print("Wrong character.")
         
if (100 >= alice[1] > bob[1] >= 1):
    ap += 1
    print("Number two. Alice receives 1 point.",ap,bp)
elif (1 <= alice[1] < bob[1] <= 100):
    bp += 1
    print("Number two. Bob receives 1 point.",ap,bp)
else:
    if ((100 >= alice[1] >=1 and 100 >= bob[1] >=1)):
        print("Number two. Values are equal.",ap,bp)
    else:
        print("Wrong character.")
if (100 >= alice[2] > bob[2] >= 1):
    ap += 1
    print("Number three. Alice receives 1 point.",ap,bp)
elif (1 <= alice[2] < bob[2] <= 100):
    bp += 1  
    print("Number three. Bob receives 1 point.",ap,bp)
else:
    if ((100 >= alice[2] >=1 and 100 >= bob[2] >=1)):
        print("Number three. Values are equal.",ap,bp)
    else:
        print("wrong character.")