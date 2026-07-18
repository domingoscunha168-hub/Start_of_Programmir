from random import randint
from math import dist
from datetime import date


def jogo_adivinhacao():
    pc = randint(0, 18)
    tentativas = 0

    print("\nJogo de adivinhacao")
    print("Pensei num numero entre 0 e 18.")

    while True:
        try:
            human = int(input("Informe sua tentativa: "))
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")
            continue

        if human < 0 or human > 18:
            print("Use um numero entre 0 e 18.")
            continue

        tentativas += 1

        if human < pc:
            print("More, tente mais vezes.")
        elif human > pc:
            print("Less, tente mais vezes.")
        else:
            print(f"Vitoria, acertou com {tentativas} tentativas.")
            break


def calcular_preco_viagem():
    print("\nCalculo do preco da viagem")

    while True:
        try:
            quilometros = float(input("Informe a distancia da viagem em km: "))
            if quilometros < 0:
                print("A distancia nao pode ser negativa.")
                continue
            break
        except ValueError:
            print("Valor invalido. Digite um numero.")

    distancia = dist((0, 0), (quilometros, 0))

    if distancia <= 200:
        preco = distancia * 0.50
    else:
        preco = distancia * 0.40

    print(f"O preco da passagem e {preco:.2f} para {distancia:.2f} km")


def verificar_ano_bissexto():
    print("\nVerificador de ano bissexto")

    while True:
        try:
            year = int(input("Qual ano deseja verificar? Use 0 para o ano atual: "))
            break
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")

    if year == 0:
        year = date.today().year

    bissexto = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    if bissexto:
        print(f"O ano {year} e bissexto.")
    else:
        print(f"O ano {year} nao e bissexto.")


def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[1] Jogo de adivinhacao")
        print("[2] Calculo do preco da viagem")
        print("[3] Verificar ano bissexto")
        print("[0] Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            jogo_adivinhacao()
        elif opcao == "2":
            calcular_preco_viagem()
        elif opcao == "3":
            verificar_ano_bissexto()
        elif opcao == "0":
            print("Fim do programa.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
