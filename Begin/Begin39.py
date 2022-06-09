import random
import math
r = list(range(-10,0)) + list(range(1,11))
A = random.choice(r)
C = random.randrange(-10,11)
B1 = math.ceil(math.sqrt(abs(4*A*C)))
#B = (random.randrange(0,2)-1)*(random.randrange(B1,B1+10))
B = random.randrange(B1,B1+10)
coef = random.choice([-1,1])
A = coef * A
B = coef * B
C = coef * C
print("Ax^2 + Bx + C = 0")
print("A = ",A)
print("B = ",B)
print("C = ",C)
D = B*B - 4*A*C
x1 = (-B - math.sqrt(D))/(2*A)
x2 = (-B + math.sqrt(D))/(2*A)
s = sorted([x1,x2])
print("D = ",D)
print(s)
print("Check x1:",A*x1*x1+B*x1+C)
print("Check x2:",A*x2*x2+B*x2+C)