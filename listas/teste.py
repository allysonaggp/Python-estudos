# Crie um programa que vai ler vários números e colocar me uma lista.
# Depois disso , mostre:
# a) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista
from operator import invert

lista = [3,6,4,8,2,4,6,9,5,6,8,4,5]
# quantidade = int(input('quantos números voce gostaria de adicionar a lista'))
# for i in range(quantidade):
#     numero = int(input('Digite o valor do numero: '))
#     lista.append(numero)
qtd_lista=len(lista)
lista.sort(invert)
print(f'Foram adicionados {len(lista)}')
