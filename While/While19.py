import random
N = random.randrange(1,10000)
print("N = ",N)
q = N
s = 0
while q >= 1:
    r = q % 10
    q = int(q/10)
    s = s*10 + r
print("Новое число:",s)