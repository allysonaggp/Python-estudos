import random
base=["1","2","3","4","5","6","7","8","9","10"]
piadinha_base = ["ixe foi quase", "nao foi desta vez", "sei que vc pode fazer melhor", "kkkkk"]
numero = 0
sorteio = random.choice(base)

print("Vamos ver se vc acerta")
print(sorteio)

numero = input("adivinhe o numero que estou pensando de 1 ate 10\n")

while numero != sorteio:
    print("Digite um numero valido")

    piadinha = random.choice(piadinha_base)
    numero = input(f"{piadinha},tente de novo\n")
print("Voce acertou! Parabens 🎉")
