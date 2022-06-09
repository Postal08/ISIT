import random
A = random.randrange(10)
n = random.randrange(10)+1
B = A + n
print('A = ', A)
print('B = ', B)
S = 0
for i in range(A,B+1,1):
    S += i*i
    print(i," : ",i*i," : ",S)
print("Sum of squares = ",S)