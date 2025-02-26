import random, os
while True:
    count = 10
    jogadorPlacar = 0
    maquinaPlacar = 0
    empatePlacar = 0
    while (count > 0):
        
        sorteio = random.randrange(1,3)
        print("====Jo-ken-po====\n\n[1]Papel\n[2]Pedra\n[3]Tesoura\n\n")
        while True:
            jogada = int(input("Digite o seu ataque: "))
            if (jogada > 0 and jogada < 3):
                break
            else:
                print("Digite um valor vailido!\n\n")
        if (jogada == sorteio):
            resultado = "Empate"
            empatePlacar += 1
        elif (jogada == 1 and sorteio == 2) or (jogada == 2 and sorteio == 3) or (jogada == 3 and sorteio == 1):
            resultado = "Jogador ganhou!"
            jogadorPlacar += 1
        else:
            resultado = "Maquina ganhou!"
            maquinaPlacar += 1
        jogador = "Papel" if jogada == 1 else "Pedra" if jogada == 2 else "Tesoura"
        maquina = "Papel" if sorteio == 1 else "Pedra" if sorteio == 2 else "Tesoura"
        print("{}\nPlacar: {}x{}\nJogador: {}\nMaquina: {}\nEmpate: {}".format(resultado,jogadorPlacar,maquinaPlacar,jogadorPlacar,maquinaPlacar,empatePlacar))
    confirma=input("Nova tentativa? [S/N]: ")
    if confirma.lower() == 'n':
        break
    else:
        os.system('cls')