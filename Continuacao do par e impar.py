import random

vitorias = 0

while True:
    
    player = input("Escolha par ou impar (p/i): ").strip().lower()
    while player not in ["p", "i", "par", "impar", "d", "m"]:
        player = input("Incorreto. Escolha par ou impar (p/i): ").strip().lower()

    
    if player in ["par", "d"]:
        player = "p"
    elif player in ["impar", "m"]:
        player = "i"

    # Numero do jogador
    while True:
        try:
            number_of_jogador = int(input("Informe um valor entre 0 e 10: "))
            if 0 <= number_of_jogador <= 10:
                break
        except ValueError:
            pass
        print("Incorreto. Informe um numero inteiro entre 0 e 10.")

    # Numero do computador
    number_of_computador = random.randint(0, 10)
    print(f"O computador escolheu: {number_of_computador}")

    # Soma
    soma = number_of_jogador + number_of_computador
    print(f"Soma: {soma}")

    # Verifica par ou impar
    if soma % 2 == 0:
        resultado = "p"
        print("Resultado: Par")
    else:
        resultado = "i"
        print("Resultado: Impar")

    # Verifica vencedor
    if player == resultado:
        vitorias += 1
        print(f"Voce venceu! Total de vitorias: {vitorias}")
    else:
        print("Derrota")
        break

print(f"Total de vitorias: {vitorias}")
