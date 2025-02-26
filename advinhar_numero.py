import random, os

while True:
    count = 5
    n = random.randrange(1,50) 
    while (count > 0):
        print("====Advinhar Numero====")
        print("\n\nTentativas: {}".format(count))
        while True:
            palpite = int(input("Digite o seu palpite: "))
            if (palpite < 50 and palpite >= 0):
                break
            else:
                print("O numero deve estar entre 0 e 50")
        saida = "Digite um numero maior" if n>palpite else "Digite um numero menor" if n<palpite else "Numero correto"
        print(saida)
        count -= 1
        if (saida == "Numero correto"):
            break
    
    confirma=input("Nova tentativa? [S/N]: ")
    if confirma.lower() == 'n':
        break
    else:
        os.system('cls')