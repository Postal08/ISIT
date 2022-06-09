import random
import numpy
M = random.randrange(2,10)
N = random.randrange(2,10)
print("M = ",M,"; N = ",N)
a = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(-5,5)
print(a)
print("Even Rows: ")
for i in range(0,M,2):
    print(a[i])
print()
Matrix = [[random.randrange(-5,5) for x in range(N)] for y in range(M)]
print(Matrix)
print("Even Rows: ")
for i in range(0,M,2):
    print(Matrix[i])
print()