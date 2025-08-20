# Desenvolva um programa que leia quatro valores pelo teclado e quarde-os em uma tupla. No f inal, mostre: a) quantoas vezes aparece o valor 9b) Em qual posi''cão foi digitado o primeiro valor 3 c) quantos foram os numeros pares
lista = []
numeros_pares = []
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Digite 4 valores para ser gerado uma tupla.')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
for c in range(0, 4):
    numero = int(input(f"Digite o {c+1} numero: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    lista.append(numero)
list_tuple = tuple(lista)
print(" \n")

if 3 in list_tuple:
    posicao = 'O valor [3] foi digitado na posição: {list_tuple.index(3)+1}'
else:
    posicao = "O numero 3 não foi encontrado"

if numeros_pares == []:
    numeros_pares = 'Não foram encontrados números pares'
else:
    numeros_pares = f'Os numeros pares foram os números: {numeros_pares}'

# questões
print(f'Voce digitou os numeros: {list_tuple}')
print(f'A) O valor [9] aparceu {list_tuple.count(9)} vezes')
print(f'B) {posicao}')
print(f'C) {numeros_pares}')

