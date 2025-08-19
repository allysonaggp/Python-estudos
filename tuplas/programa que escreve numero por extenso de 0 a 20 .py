# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte. Seu  programa deverá ler um numero pelo teclado entre 0 e 20 e mstra-lo por extenso
base_numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('digite um numero de 0 a 20: '))
    if numero > 0 and numero < 20:
        print(f"Voce digitou {base_numero[numero]}")
    else:
        print("Tente novamente. Digite um numero entre 0 e 20")
