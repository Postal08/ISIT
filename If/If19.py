import random
def RandNum():
    l = []    
    x1,x2 = random.sample(range(-10, 10), 2)
    N = random.randrange(1,5)
    if N == 1:
        l.append(x2)
        l.append(x1)
        l.append(x1)
        l.append(x1)
    elif N == 2:
        l.append(x1)
        l.append(x2)
        l.append(x1)
        l.append(x1)
    elif N == 3:
        l.append(x1)
        l.append(x1)
        l.append(x2)
        l.append(x1)
    else:
        l.append(x1)
        l.append(x1)
        l.append(x1)
        l.append(x2)
    return l
        
A,B,C,D = RandNum()
print("Число A:", A)
print("Число B:", B)
print("Число C:", C)
print("Число D:", D)
if A == B:
    if A == D:
        print("C")
    else:
        print("D")
else:
    if A == C:
        print("B")
    else:
        print("A")