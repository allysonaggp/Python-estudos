# faça um programa que  leia o sexo da pessoa, mas so aaceite os valores "M" ou "F". Caso esteja errado, peça a digitacão novamente até  ter um valor correto
sexo = ["m", "f"]
resposta = ""
# o "not in" verifica se a variavel"resposta" esta contida na lista "sexo"
while resposta.lower() not in sexo:
    resposta = str(input("digite um sexo [M/F]\n"))
