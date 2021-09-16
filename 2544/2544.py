def calcula_tecnica(ninjas):
    i = 1
    cont = 0
    while i != ninjas:
        i *= 2
        cont += 1
    return cont

while True:
    try:

        ninjas = int(input())
    
        if ninjas > 1:
            resultado = calcula_tecnica(ninjas)
        else:
            resultado = 0

        print(resultado)
    except EOFError:
        break