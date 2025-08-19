frase = "   curso em video python"
frase2= "o melhor que nos temos"
print(frase[3:6])
# o "len" e equiparado ao lenght  no JS
print(len(frase))
# o .count("o") mostra quantas vezes a letra "o" apareceu
print(frase.count('o'))
# serve para procurar em qual posiçao esta alocado
print(frase.index("o"))
# quando retorna o valor -1 e porque ele nao existe
print(frase.find("deo"))
# o "in" verifica se a palavara "video" esta dentro do objeto "frase"
print("video" in frase)
# o ".replace" troca a string por outra strig
print(frase.replace("python", "java script"))
print(frase)
frase = frase.replace("python", "java script")
print(frase)
# o metodo ".upper" deixa toda string em caixa alta
print(frase.upper())
# o metodo ".lower" deixa toda a string em caixa abaixa
print(frase.lower())
# print(frase.capitalize())
# o metodo ".title" deixa todo inicio de palavra com caixa alta
print(frase.title())
# o metodo".strip"retira os espaços iniciais e finais das strings
# tendo as variaços com "l" e "r" antes do strip
print(frase.strip())
# retira espaço no início
print(frase.lstrip())
# retira espaço no final
print(frase.rstrip())
# junta todos os elementos da lista em string
print("".join(frase))
# transfoma a string em uma lista para poder ser manipulada
print(frase.split())
print(frase)

fraseCompleta =frase.split()+frase2.split()
fraseCompleta =" ".join(fraseCompleta)
fraseCompleta = fraseCompleta.capitalize()
fraseCompleta = fraseCompleta.split()
fraseCompleta[5] = ". O"
fraseCompleta = " ".join(fraseCompleta)
fraseCompleta = fraseCompleta.replace(" .", ".")
fraseCompleta = fraseCompleta.split()
fraseCompleta = "-".join(fraseCompleta)
fraseCompleta = fraseCompleta+"."

print(fraseCompleta)



# função de saudação
def saudacao(nome):
    return f"Ola {nome.upper()}, é um prazer imenso te conhcer!!"

# nome = input("Oi tudo bom como vc se chama\n")
# print(saudacao(nome))
