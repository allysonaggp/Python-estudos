def somador_numeros_impares(inicio,fim):
    numero = 0
    for i in range(inicio,fim):
       if i % 3 == 0:
           numero+=i
    print(numero)


somador_numeros_impares(250,500)