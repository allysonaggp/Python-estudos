# # Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas externas que vão conter numero pares os
# os numeros impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas

lista = []
numeros_pares = []
numeros_impares = []
quantidade = int(input('Digite quantos numero voce quer adicionar a lista: '))
for i in range(quantidade):
    lista.append(int(input('Digite um valor: ')))
    if lista[i] % 2 == 0:
        numeros_pares.append(lista[i])
    else:
        numeros_impares.append(lista[i])
print(f'\nlista dos números{lista}'
      f'\nnúmeros pares: {numeros_pares}'
      f'\números ímpares: {numeros_impares}')