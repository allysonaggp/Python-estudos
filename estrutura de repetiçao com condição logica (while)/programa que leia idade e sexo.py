# crie um programa que leia a idade eo sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) qunatas pessoas tem mais de 18 anos. b) Quantos  homens foram cadastrado. c) Quantas mulheres tem menos de 20 anos
pessoas_maiores_18 = 0
feminino_menor_20 = 0
masculino = 0

print("Cadastro de pessoas")
while True:
    sexo = " "
    resposta = " "

    nome = input("\nDigite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))

    while sexo not in "MF":
        sexo = input("Digite o sexo do cliente [M/F]: ").strip().upper()[0]

    if sexo == "M":
        masculino += 1
    if sexo == "F" and idade < 20:
        feminino_menor_20 += 1
    if idade > 18:
        pessoas_maiores_18 += 1

    while resposta not in "SN":
        resposta = input("Deseja continuar? (S/N)").strip().upper()[0]
    if resposta == "N":
        break


print("Cadastro de pessoas\n")
if pessoas_maiores_18 > 0:
    print(f"Existem {pessoas_maiores_18} pessoas maiores de 18 anos\n")
if masculino > 0:
    print(f"Existem {masculino} homens cadastrados\n")
if feminino_menor_20 > 0:
    print(f"Existem {feminino_menor_20} mulheres menores de 20 anos")
