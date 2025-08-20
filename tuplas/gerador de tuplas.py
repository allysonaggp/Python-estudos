# Crie um programa que vaio gerar números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de nnúmeros gerados e também indique o menos e o maior valor que estão na tupla
import random

lista = []
menor_num = 0
maior_num = 0
for c in range(0, 5):
    num = random.randint(1, 50)
    lista.append(num)

    if menor_num == 0:
        menor_num = num
    if num < menor_num:
        menor_num = num
    if num> maior_num:
        maior_num = num

lista2 = tuple(lista)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
      'Gerador de Tuplas\n'
      '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
print(f"A lista de numero é:\n"
      f" {lista2}")
print(f"O maior numero da tupla é: {maior_num}")
print(f"O menor numero da tupla é: {menor_num}")
