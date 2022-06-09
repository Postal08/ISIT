import random
N = random.randrange(2,21)
#N = 15
a = [random.randrange(1,10) for i in range(N)]
##N = 12
##a = [6, 5, 3, 5, 5, 2, 4, 9, 8, 8, 2, 6]
##a = [3, 3, 1, 8, 9, 6, 9, 2, 6, 6, 2, 6, 2, 9, 6]
#a = [7, 2, 1, 8, 2, 8, 6, 9, 9, 2, 2, 2, 8, 9, 5]
##for i in range(0,N):
##    a[i] = N - i
##a[7] = 0
##a = [17, 13, 15]
print("N = ", N)
print("Array:")
print(a)
dec_k = 0
dec_flag = True
for i in range(1,N):
    if a[i-1] > a[i] :
        if dec_flag:
            dec_k += 1
            dec_flag = False
    else :
        dec_flag = True
print("Monotonous Decrease intervals:",dec_k)
inc_k = 0
inc_flag = True
for i in range(1,N):
    if a[i-1] < a[i] :
        if inc_flag:
            inc_k += 1
            inc_flag = False
    else :
        inc_flag = True
print("Monotonous Increase intervals:",inc_k)
print("Monotonous intervals:",inc_k+dec_k)
import matplotlib.pyplot as plt
plt.plot(a)
plt.show()