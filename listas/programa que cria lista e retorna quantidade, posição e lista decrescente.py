# Crie um programa que vai ler vários números e criar uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista


lista = []
quantidade = int(input('quantos números voce gostaria de adicionar a lista: '))
for i in range(quantidade):
    numero = int(input('Digite o valor do numero: '))
    lista.append(numero)

qtd_lista = len(lista)
lista.sort(reverse=True)

print(f'\nA lista contem {qtd_lista} números')
print(f'Os valores de ordem decrescente são: {lista}')
if 5  in lista:
    print(f'O número 5 esta na posição: {lista.index(5)} da lista')
