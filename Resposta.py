resposta = ""

while resposta != "N":
    resposta = input("Quer continuar? [S/N] ").strip().upper()[:1]
    while resposta not in ("S", "N"):
        resposta = input("Resposta invalida. Digite apenas S ou N: ").strip().upper()[:1]

print("Programa encerrado.")
