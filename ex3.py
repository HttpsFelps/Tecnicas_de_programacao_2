def calculo():
    print("Aluno {} com media {}".format(situacao, media))

while True:
    n1 = int(input("Digite a nota 1: "))
    n2 = int(input("Digite a nota 2: "))
    n3 = int(input("Digite a nota 3: "))

    media = round((n1+n2+n3)/3,2)
    if (media<4):
         situacao = "reprovado"
    elif (media>=4 and media < 6):
        situacao = "recuperacao"
    else:
        situacao = "aprovado"
    calculo()
    confirma=input("novo calculo? [S/N]: ")
    if confirma.lower() == 'n':
        break

