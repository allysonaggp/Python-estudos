
def testador_de_numero_primo():
    numero = int(input("Digite um numero: "))
    for i in range(1, numero + 1):
        if numero == 2 or numero == 3 or numero % i == 0 and numero % 2 != 0 and numero % 3 != 0:
            numero="primo"
            print(numero)
        else:
            numero="não é primo"
            print(numero)

testador_de_numero_primo()