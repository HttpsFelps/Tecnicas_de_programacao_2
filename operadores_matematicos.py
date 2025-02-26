import random,os
count = 0
def exibir_result():
    print("\n\n\nQTDE acertos: {}".format(count))

while True:
    os.system('cls')
    n1 = random.randrange(1,10)
    n2 = random.randrange(1,10)
    opRand = random.randrange(1,3)
    op = "+" if opRand == 1 else "-" if opRand == 2 else "*"
    result = n1 + n2 if op == "+" else n1 - n2 if op == "-" else n1 * n2
    print("=====Operadores====\n\n\n")
    resultInput=int(input("{} {} {} = ".format(n1,op,n2)))
    if (result == resultInput):
        count += 1
    exibir_result()
    confirma=input("novo calculo? [S/N]: ")
    if confirma.lower() == 'n':
        break