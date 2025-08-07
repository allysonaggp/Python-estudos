# Bibblioteca time
import time

print("ola tudo bem")
time.sleep(2)

print("sou seu assistente de aumento de Salario\n")
time.sleep(2)

salario = float(input("Digite o valor do seu salario por favor\n"))
time.sleep(2)

aumento = float(input("Digite o percentual do seu aumento sem o %: \n"))
print("ok aguarda um momento que vou processar os dados . . .")
time.sleep(2)

valorAumento = (salario * (aumento / 100))
valorComAumento = valorAumento + salario
print("Ainda estou calculando, um momento . . .\n")
time.sleep(2)

print(f"O Valor do deu Salário com o Aumento fica no valor de R$:{valorComAumento:.2f} Reais, referente ao valor de {salario:.2f} + {valorAumento:.2f} de acrescimo")
