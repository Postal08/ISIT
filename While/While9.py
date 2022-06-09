import random
N = random.randrange(2,1000)
#N = 100
print('N = ', N)
K = 0
P = 1
while P <= N:
    P *= 3
    K += 1
print("K = {0}, 3^K = {1}, 3^(K-1) = {2}".format(K,3**K,3**(K-1)))