import random
U,V = sorted(random.sample(range(10, 21), 2))
T1,T2 = [random.randrange(1,6) for i in range(2)]
Distance_Lake = V * T1
Distance_River = (V - U) * T2 
print("Speed in the lake:",V)
print("Speed of the river:",U)
print("Speed in the river (up the stream):",V-U)
print("Time in the lake:",T1)
print("Time in the river:",T2)
print("Path in the lake:",Distance_Lake)
print("Path in the river:",Distance_River)