def julga_partida(sheldon,raj):
    mensagem_vitoria = "Bazinga!"
    mensagem_derrota = "Raj trapaceou!"
    mensagem_empate = "De novo!"
    if ((sheldon == "tesoura" and raj == "papel") or (sheldon == "papel" and raj == "pedra") or 
        (sheldon == "pedra" and raj == "lagarto") or (sheldon == "lagarto" and raj == "Spock") or
        (sheldon == "Spock" and raj == "tesoura") or (sheldon == "tesoura" and raj == "lagarto") or
        (sheldon == "lagarto" and raj == "papel") or (sheldon == "papel" and raj == "Spock") or
        (sheldon == "Spock" and raj == "pedra") or (sheldon == "pedra" and raj == "tesoura")):
        return mensagem_vitoria
    elif sheldon == raj:
        return mensagem_empate
    else:
        return mensagem_derrota
    

jogadas = {}
tentativas = int(input())
for i in range (0,tentativas):
    jogadas[i] = input().split()
    print(f"Caso #{i+1}: {julga_partida(jogadas[i][0],jogadas[i][1])}")