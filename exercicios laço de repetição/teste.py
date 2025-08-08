# Desenvolva um programa que leia o primeiro termo e a razao de um PA. No final, mostre os 10 primeiros rtermos dessa progressão.
print("Listador de numeros de uma Progressão Aritimetica\n")
primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite o valor da razão da progressão aritimetica: "))
qtd_termos = int(input("Digite a quantidade de termos: \n"))

def lista_progressao_aritimetica(primeiro_termo, razao, qtd_termos):
    lista = [primeiro_termo]
    for i in range(qtd_termos):
        primeiro_termo = primeiro_termo + razao
        lista.append(primeiro_termo)
    print (lista)

lista_progressao_aritimetica(primeiro_termo, razao, qtd_termos)