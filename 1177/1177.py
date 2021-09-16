n = {}
t = int(input())
cont = 0

for i in range(0,1000):
    if cont < t:
        n[i] = cont
        cont+=1
    else:
        cont = 1
        n[i] = 0
    print(f"N[{i}] = {n[i]}")