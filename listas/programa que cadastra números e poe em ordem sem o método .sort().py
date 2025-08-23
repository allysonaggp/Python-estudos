# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista,ja na posição correta de inserção( sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
quantidade=int(input('Quantos números vc deseja acrescentar na lista: '))
for i in range(quantidade):
    numero = int(input('Digite um numero: '))
    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f'Numero {numero} adicionado ao final da lista')
    else:
        cont = 0
        while cont < len(lista):
            if numero<=lista[cont]:
                lista.insert(cont, numero)
                print(f'Numero {numero} adicionado na posição {cont+1}')
                break
            cont += 1

print(f'\nForam digitados os números:'
      f'\n{lista}')
