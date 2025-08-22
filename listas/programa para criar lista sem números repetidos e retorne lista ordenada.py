# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastra-los em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []

resposta = "S"
while resposta == 'S':
    numero = input('Digite um numero: ')
    if numero.isdigit() and numero not in lista:
        lista.append(numero)
        print(f'Numero {numero} foi adicionado com sucesso')
    elif numero in lista:
        print('Numero já cadastrado')
    else:
        print('Digite um numero valido')

    resposta = input('Gostaria de continuar [S/N]').strip().upper()[0]
    if resposta == "N":
        lista.sort()
        if len(lista)==0:
            print('\n=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                  '\nnão tiveram números cadastrados')
        else:
            print('\n=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                  f'\nOs número cadastrados foram {lista}')
        break

