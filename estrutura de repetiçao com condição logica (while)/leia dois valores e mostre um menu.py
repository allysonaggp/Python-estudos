# Crie um programa que leia dois valores e mostre um menu na tela:
print("Menu de interação com numeros\n")
n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
n=0



while n != 5:
    print("\nMenu de interação com numeros")
    print("Digite para realizarmos a ação:")
    n = int(input("[1] Somar\n"
                  "[2] Multiplicar\n"
                  "[3] Ver qual numero e maior\n"
                  "[4] Novos numeros\n"
                  "[5] Sair do programa\n"))
    if n == 1:
        print(f"a soma de {n1} + {n2} é = {n1 + n2}")
    if n == 2:
        print(f"a multiplicação de {n1} x {n2} é = {n1 * n2}")
    if n == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        else:
            print(f"{n2} é maior que {n1}")
    if n == 4:
        n1 = int(input("digite o primeiro numero\n"))
        n2 = int(input("digite o segundo numero\n"))
    if n == 5:
        print("Ate mais ")
