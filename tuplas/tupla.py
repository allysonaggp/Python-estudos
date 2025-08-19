lanche = ("hamburguer", "suco", "pizza", "pudim")
# tuplas sao imuaveis
for comida in lanche:
    if comida == "suco":
        print(f"eu tomei {comida}")
    else:
        print(f"eu comi {comida}")
print(f"eu comi pra caramba !!\n"
      f""
      f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

for cont in range(0, len(lanche)):
    if cont == 0:
        print(f"eu comi {lanche[0]}", end=",")
    elif cont == (lanche[-2]):
        print(f" {lanche[cont]}", end="e ")
    else:
        print(f"{lanche[cont]}",end="")