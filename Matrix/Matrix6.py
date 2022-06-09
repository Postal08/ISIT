import random
import numpy
M = random.randrange(2,10)
N = random.randrange(2,10)
Q = random.randrange(-5,5)
print("M = ",M,"; N = ",N,"; Q = ",Q)
a = numpy.zeros((M, N))
c = [random.randrange(1,5) for i in range(N)]
print("Набор из ",N," чисел:")
print(c)
print()
for i in range(M):
    for j in range(N):
        a[i][j] = c[j]*Q**i
print(a)
print()
Matrix = []
for i in range(M):
    Matrix.append([c[j]*Q**i for j in range(N)])
print(Matrix)