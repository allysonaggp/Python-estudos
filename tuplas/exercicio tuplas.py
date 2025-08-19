# Crie uma tupla com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebbol, na ordem de colocaçao. Depois mostre:: a) apenas os primeiros colocados b) os últimos colocados da tabela c) Uma lista com os times em ordem alfabetica. d)Em que posiçao da tabela esta o time do Sport
times_brasileirao = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Fluminense', 'RB Bragantino', 'Ceará', 'Atlético-MG', 'Internacional', 'Grêmio', 'Corinthians', 'Santos', 'Vasco', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
      "Campeonato Brasileiro 2024\n"
      "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
# Os 5 primeiros colocados
print(f"Os 5 primeiros colocados.\n"
      f"{times_brasileirao[0:5]}")
print("***********************************")
# Os 4 últimos colocados
print(f"Os 4 últimos colocados.\n"
      f"{times_brasileirao[-4:]}")
print("***********************************")
# Os tímes em ordem alfabética
print(f"Os times em ordem alfabética.\n"
      f"{sorted(times_brasileirao)}")
print("***********************************")
# Posição do tíme do Sport
print(f"O time do Sport esta na posição: {times_brasileirao.index('Sport')} do Brasileirão.")
print(times_brasileirao)
