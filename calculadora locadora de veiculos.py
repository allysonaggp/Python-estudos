# Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a qauntidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$:60 por dia e R$:0,15 por Km rodado.
kmRodado = int(input("Digite quantos quilometros foram percorridos: "))
qtdDias = int(input("Digite quantos dias o carro foi alugado: "))

precoAPagar = (qtdDias * 60) * (kmRodado * 0.15)
print(f"\nTotal a pagar R$:{precoAPagar:.2f} Reais por {qtdDias} dias e {kmRodado} km rodado.")
