# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de três e que se encontram no intervalo de 1 ate 500

# aqui definimos quando o numero e impar
# numeros_impares = numero % 3 == 0


# intervalo
def numeros_no_impar_no_intervalo(numero):
    print(f"Calculadora de numeros impares no intervalo de 0 e {numero}\n")
    numeros_impares = 0
    grupo_numeros_impares = []
    for i in range(1, numero):
        if i % 3 == 0:
            numeros_impares = numeros_impares + i
            grupo_numeros_impares.append(i)
    print(f"Os numeros impares entre 0 e {numero} são: \n{grupo_numeros_impares}")
    print(f"\nA soma de todos os numeros é: {numeros_impares}")


numeros_no_impar_no_intervalo(12)
