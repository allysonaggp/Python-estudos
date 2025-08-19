# crie um programa que leia o nome e o preço de vários produtos.O programa  deverá perguntar se o usuário vai continuar. no final, mostre: a) qqqual o total gasto na compra ,) qauntos produtos custarram mais de R$:1.000, c) qqual o nome do produto mais barato
total_gasto = 0
produtos_caros = 0
nome_produto_barato = " "
produto_mais_barato = 0
continuar = " "


while continuar != "N":
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("BEM VINDO A BARRAQUINHA  DO SEU ZÉ 🛒")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    produto = input("digite o nome do produto: ")
    preco = float(input("digite o valor do produto: "))

    total_gasto += preco

    if preco > 1000:
        produtos_caros += 1

    if produto_mais_barato == 0:
        produto_mais_barato = preco
        nome_produto_barato = produto

    if preco < produto_mais_barato:
        produto_mais_barato = preco
        nome_produto_barato = produto

    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    continuar = str(input("deseja continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        print(f"Total gasto na compra {total_gasto:.2f}")
        print(f"Tiveram {produtos_caros} produtos com valor acima de  R$:1000,00")
        print(f"E o produto mais barato foi o {nome_produto_barato}, custando {produto_mais_barato:.2f} reais.")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
