entrada1 = input()
entrada2 = input()

peca1 = entrada1.split()
peca2 = entrada2.split()

valor_total = (int(peca1[1])*float(peca1[2])+int(peca2[1])*float(peca2[2]))

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
