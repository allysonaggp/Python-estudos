# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastra-los em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []

while True:
    numero = int(input('Digite um numero: '))
    print('para sair digite [0]')
    if numero not in lista:
        lista.append(numero)
    elif numero == 0:
        break
    else:
        print('Numero já cadastrado')
    lista.sort()
    print(lista)