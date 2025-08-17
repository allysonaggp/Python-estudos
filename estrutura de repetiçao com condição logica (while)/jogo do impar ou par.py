import random

print("ola vamos jogar🕹️")
player = 3
cpu = "impar"
vitorias = 0

while player != 0:
    player = int(input("Escolha entre impar ou par\n\n"
                       "✅[1] - para Impar\n"
                       "✅[2] - para Par\n"
                       "❌[0] - para sair\n"))
    if player == 1:
        player = "impar"
        cpu = "par"
        print(f"🟢 O jogador escolheu {player}")
        print(f"🔴 O computador escolheu {cpu}")
        nc = random.randint(1, 11)
        # print(nc)
        np = int(input("Escolha um numero de 0 a 10\n"))
        if (nc + np) % 2 == 0:
            print(f"🔴 O computador escolheu {nc}\n"
                  f"🟢 O jogador escolheu {np}\n")
            print(f"🔴 O computador ganhou 🏆\n\n"
                  f"O jogador teve um total de {vitorias} vitórias consecutivas\n"
                  f"----------------------------------------------")

            break
        else:
            print(f"🔴 O computador escolheu {nc}\n"
                  f"🟢 O jogador escolheu {np}\n")
            print(f"🟢 O Jogador ganhou 🏆\n\n"
                  f"-------------------------\n")
            vitorias += 1

    elif player == 2:
        player = "par"
        cpu = "impar"
        print(f"🟢 O jogador escolheu {player}")
        print(f"🔴 O computador escolheu {cpu}")
        nc = random.randint(1, 11)
        # print(nc)
        np = int(input("Escolha um numero de 0 a 10\n"))
        if (nc + np) % 2 == 0:
            print(f"🔴 O computador escolheu {nc}\n"
                  f"🟢 O jogador escolheu {np}\n")
            print("🟢 O jogador ganhou 🏆\n\n"
                  "--------------------------\n")
            vitorias += 1
        else:
            print(f"🔴 O computador escolheu {nc}\n"
                  f"O jogador escolheu {np}\n")
            print("🔴 O computador ganhou  🏆\n\n"
                  f"O jogador teve um total de {vitorias} vitórias consecutivas\n"
                  f"----------------------------------------------")
            break
