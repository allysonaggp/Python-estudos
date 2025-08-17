from itertools import count

n = s = 0
lista = []
while True:
    lista.append(n)
    n = int(input("digite o valor de um numero: "))
    if n == 0:
        break
    s += n

print(f"Os numeros digitados foram{str(lista)[3:-1]} e a soma deles é {s}")
