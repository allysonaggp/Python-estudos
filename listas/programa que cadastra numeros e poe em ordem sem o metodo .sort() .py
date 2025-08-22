# metodo .append() adiciona o elemento ao final da lista
# o metodo .insert(0,'') adiciona o item com o local  selecionado pelo novo item atribuido
# lista[1]="jacare" troca o item selecionado
# para deletar podemos usar o del+lista+[posiçao]   ou o metodo lista.pop[posição]
# lista.remove("nome do item da lista") remove o item da lista
lista = ['cachorro', 'calavo', 'gato']
lista.insert(1, "baleia")
print(lista)

valores = list(range(1, 12))
print(valores)

lista = [88, 6, 2, 4, 9, 7, 5, 8, 3, 7, 1, 5, 87, ]
# o metodo .sort() ordena todos os itens da lista
lista.sort()
print(lista)
# o metodo .sort(reverse=True) mostra a lista de modo reverso
lista.sort(reverse=True)
print(lista)

# valores = list()
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# for c,f in enumerate(valores):
#     print(f'na posição {c} encontrei o valor {f}')
# print('Cheguei ao final da lista')

# quando declaramos "b=a" eles criam uma relaçao
a = [2, 3, 4, 7]
b = a
b[2]=8
print(a) #[2, 3, 8, 7] o trerceiro item da lista "a" é igual ao da lista "b"
print(b) #[2, 3, 8, 7]

 # mas quando fatiamos usando [:] ele cria de fato uma cópia da lista

a = [2, 3, 4, 7]
b = a[:]
b[2]=8
print(a) #[2, 3, 4, 7]
print(b) #[2, 3, 8, 7]
# perceba que aqui o terceiro ítem da lista "b"
# é diferente do terceiro ítem da lista "a"..
