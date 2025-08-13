
# Digite o nome do aluno
aluno = input("Digite o nome do aluno: \n")

# Digite a primeira nota
nota1 = int(input("Digite a primeira nota : \n"))
while nota1 > 10 or nota1 <= 0:
    print("Digite uma nota com o valor correto\n")
    nota1 = int(input("Digite a primeira nota : \n"))

# Digite a segunda nota
nota2 = int(input("Digite a segunda nota: \n"))
while nota2 > 10 or nota2 <= 0:
    print("Digite a nota com o valor correto\n")
    nota2 = int(input("Digite a segunda nota: \n"))

#Calculo da media dos alunos
media = (nota1 + nota2) / 2

# Situação da aprovção dos alunos
if media < 6:
    situacao = "reprovado"
else:
    situacao = "aprovado"

# Retorno no terminal de todo o compilado
print("O aluno {} foi {} com média {}".format(aluno, situacao, media))

if situacao == "reprovado":
    print("Estude mais!!")
else:
    print("Parabens!!")
