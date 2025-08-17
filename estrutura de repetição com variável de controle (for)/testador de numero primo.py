def testador_de_numero_primo():
    numero = int(input("Digite um numero: "))
    if numero < 2:
        print("Nao e primo")
        return

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("Não é primo")
            return

    print("é primo")


testador_de_numero_primo()
