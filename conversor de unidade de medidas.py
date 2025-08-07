medida = float(input("Insira sua medida em metros: "))
print("Voce gostaria de ver o seu valor inserido em: \n")
escolha = int(input("Digite (1) para milimetro \nDigite (2) para centimentro\n\n"))

if escolha == 2:
    centimetro = float(medida * 100)
    print("Sua media em centimetros é: {}".format(centimetro))
elif escolha == 1:
    milimetro = float(medida * 1000)
    print("Sua medida em milimetros é: {}".format(milimetro))


