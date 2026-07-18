from pathlib import Path
import runpy


PROGRAMAS = [
    "programa_01_veiculo.py",
    "programa_02_formas.py",
    "programa_03_pagamentos.py",
    "programa_04_notificacoes.py",
    "programa_05_animais.py",
    "programa_06_banco.py",
]


def main():
    pasta_atual = Path(__file__).resolve().parent

    for nome_arquivo in PROGRAMAS:
        print(f"\n=== {nome_arquivo} ===")
        runpy.run_path(str(pasta_atual / nome_arquivo), run_name="__main__")


if __name__ == "__main__":
    main()

