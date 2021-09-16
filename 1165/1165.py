numero_teste = int(input())

eh_primo = True

for i in range(0,numero_teste):
    n1 = int(input())

    for c in range(2,n1):
        if n1 % c == 0:
            eh_primo = False
            break
        else:
            eh_primo = True
    if eh_primo == True:
        print(f"{n1} eh primo")
    else:
        print(f"{n1} nao eh primo")