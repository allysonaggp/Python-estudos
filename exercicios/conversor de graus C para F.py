print("=== Calculadora de conversão de temperaturas ===\n")

print("Ola tudo bem!")
print("vamos fazer conversão de temperaturas comigo.\n")
print("Digite: ")
escolha = input("( 1 ) - para converter de Celcius para farenheit.\n( 2 ) - para converter de farenheit para Celcius.\n")
if escolha == "1":
    celcius = float(input("Digite o valor da temperatura: \n"))
    farenheit = (celcius * 1.8) + 32
    print(f"{celcius} Graus Celcius é igual a {farenheit:.2f} Graus Farenheit. ")
elif escolha == "2":
    farenheit = float(input("Digite o valor da temperatura: \n"))
    celcius = (farenheit-32)*1.8
    print(f"{farenheit} Graus Farenheit é igual a {celcius:.2f} Graus Celcius. ")