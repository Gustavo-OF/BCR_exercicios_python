testes = int(input())
entradas = {}
for i in range(0,testes):
    entradas[i] = input().split()
    if entradas[i][0] == "Thor":
        print("Y")
    else:
        print("N")