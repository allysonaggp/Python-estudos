produto = input("Por favor digite o nome do produto\n")
valor = float(input("Por favor digite o valor do produto\n"))
desconto = float(input("Por favor digite o valor da percentagem do desconto de 10 a 30\n"))
while desconto > 30 or desconto < 10:
    print("Digite um valor de desconto valido")
    desconto = float(input("Por favor digite o valor da percentagem do desconto de 10 a 30\n"))
valordoDesconto = float(valor * (desconto / 100))
valorComDesconto = float(valor-valordoDesconto)

print(f"O {produto} esta em promoção saindo há R$:{valorComDesconto}Reais com {desconto}% de desconto")
