# Desenvolva um programa que leia seis numeros interiros e  monstre a soma apenas daqueles que forem pares. Se o valor digitado for impar,desconsidere-o

def calculadora_de_numeros_pares_inteiros(numero):
    lista_de_numeros = []
    soma_numeros_pares_inteiros = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            lista_de_numeros.append(i)
            soma_numeros_pares_inteiros += i

    return (f"Lista dos numeros inteiros pares:\n{lista_de_numeros}\n"
            f"A soma dos numeros pares é: {soma_numeros_pares_inteiros}")




print(calculadora_de_numeros_pares_inteiros(6))
