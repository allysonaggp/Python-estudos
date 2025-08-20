lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
texto="LISTAGEM DE PREÇOS"
print('-'*31)
print(f'{texto:^30}')
print('_'*31)
for cont in range(0,len(lista)):
    if cont%2==0:
        print(f'{lista[cont]:.<22}',end="")
    else:
        print(f'R$:{lista[cont]:6.2f}')
