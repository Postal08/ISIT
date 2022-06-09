import random
N = random.randrange(1,15)
eps = 1/10**N
print("N = ",N)
print("eps = ",eps)
A1 = 1
A2 = 2
A3 = (A1 + 2*A2)/3
print(1,":",A1)
print(2,":",A2)
print(3,":",A3)
k = 3
while abs(A3 - A2) >= eps:
    A2, A3 = A3, (A2 + 2*A3)/3
    k += 1
    print(k,":",A3)
print()
print(k,":",A2,":",A3)