def main():
    print("Financiamento de veiculos")
    valor = float(input("Digite o valor do veiculo: "))
    while True:
        entrada = float(input("Digite o valor que deseja pagar de entrada: "))
        if entrada > valor:
            print("A entrada nao pode ser maior que o valor do veiculo")
        else:
            break
    while True:
        plano = int(input("Digite o plano de pagamento, escolha entre 12, 24, 36 ou 48 meses: "))
        if plano == 12 or plano == 24 or plano == 36 or plano == 48:
            break
        else:
            print("Plano de pagamento invalido, tente novamente")
    ano = int(input("Digite o ano do veiculo: "))

    valorfinan = valor - entrada

    #ternario em python
    juros = 1.128 if plano == 12 else 1.245 if plano == 24 else 1.324 if plano == 36 else 1.417

    parcela = round((valorfinan * juros)/plano,2)

    print("O valor finaciado é {}\nCom um plano de pagamento de {} meses\nO valor da parcela com juros aplicados é de {}".format(valorfinan,plano,parcela))

    ipva = valor * 0.04 if ano > 1995 else 0
    if ipva != 0:
        print("O valor do IPVA é de {}".format(ipva))

    total = round((parcela * plano + entrada + ipva),2)
    print("O valor total a ser pago é de {}".format(total))

while True:
    main()
    confirma=input("novo calculo? [S/N]: ")
    if confirma.lower() == 'n':
        break

