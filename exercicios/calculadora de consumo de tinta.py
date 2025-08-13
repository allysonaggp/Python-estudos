import time

print("Ola sou sua calculadora de consumo de tinta.\n")
time.sleep(1)

print("Vamos trabalha!\n")
time.sleep(2)

altura = int(input("preciso que vc digite a altura de sua parede a ser pintada: \n"))
time.sleep(2)

largura = int(input("Agora preciso que vc digite a largura da parede a ser pintada: \n"))
print("Tendo em vista que um litro de tinta pinta 2m²")
time.sleep(1)

print("Deixa eu pensar . . .\n")
time.sleep(3)

area = altura * largura
print(f"Um que legal temos uma area de {area}m²")
litrosDeTinta = area / 2
time.sleep(4)

print(f"Acredito que com {litrosDeTinta}litros de tinta conseguimos pintar os {area}m² de area")
