# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
n=2
while n>=0:
    n = int(input("Digite um numero para criar a tabuada: "))
    if n>1:
        for c in range(1,10):
            print(f"{n}x{c}={n * c}")
    else:
        print("finalizado")
