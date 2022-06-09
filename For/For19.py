import random
B = random.randrange(-9,11)
A = random.randrange(-10,B)
N = random.randrange(2,11)
H = (B - A) / N
print("A = ",A)
print("B = ",B)
print("N = ",N)
print("H = ",H)
x = A
for i in range(0,N):
    print(x,end=", ")
    x += H
print(x)