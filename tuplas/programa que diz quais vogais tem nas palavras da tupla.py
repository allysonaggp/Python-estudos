# Crie um programa que tenha uma tupla com várias palavaras. Depois disso, deve postar para cada palavra, quais são suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'tralhar',
            'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'[{letra.lower()}]',end=' ')
