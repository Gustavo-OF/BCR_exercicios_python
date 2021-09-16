n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

valores = [n1, n2, n3, n4, n5]

pares = 0

for i in valores:
    if i % 2 == 0:
        pares += 1
print(f"{pares} valores pares")

