# Faça um programa que leia 5 valores numéricos e quarde-os em uma lista.
# No final, mostre qual o maior e menor valor digitado e as suas respectivas posições na lista

lista = list()
maior = 0
menor = 0
texto = "VAMOS CRIAR UMA LISTA"
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'{texto:^42}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for cont in range(0, 5):
    numero = int(input(f'digite um numero para a posição {cont + 1}: '))
    lista.append(numero)
    if numero > maior:
        maior = numero
    if menor == 0:
        menor = numero
    if numero < menor:
        menor = numero

print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
      f'\nA lista contem os numeros{lista}'
      f'\nO maior numero foi [{maior}] e esta na posição [{lista.index(maior) + 1}]'
      f'\nO menor numero foi [{menor}] e esta na posição [{lista.index(menor) + 1}]')
