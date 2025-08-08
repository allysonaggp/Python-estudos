import random

# função geradorda de password
def gerador_de_password(tamanho=10):
    # base de caracters
    base = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789!@#$%?&*+="
    # aqui e sorteado aleatoriamente os caracters da base e adicionado a senha
    senha = "".join(random.choice(base) for i in range(tamanho))

    print(f"==password==\n {senha}")


gerador_de_password()
