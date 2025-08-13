# faá um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio, indo de 10 até 0, com uma paude de 1 segundo entre eles
import time
def show_de_fogos(tempo):
    print("Contagem regressiva para os showw de fogos")
    for i in range(tempo,0,-1):
        print(i)
        time.sleep(1)

show_de_fogos(10)

print(" 🧨🧨Booooom!🧨🧨")
print("🔥🔥🔥fogos🔥🔥🔥")
