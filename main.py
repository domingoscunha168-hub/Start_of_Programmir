from projeto_publico.livro import Livro
from projeto_publico.utils.moeda import decrementar, incrementar


def demo_moeda():
    preco = 100.0
    preco_com_aumento = incrementar(preco, 200)
    preco_com_desconto = decrementar(preco, 26)

    print(f"Com aumento de 200%: {preco_com_aumento:.2f} R$")
    print(f"Com desconto de 26%: {preco_com_desconto:.2f} R$")


def demo_livro():
    livro1 = Livro("completo", "duravel", 0, titulo="Livro Demo", autor="Equipe")
    print(livro1.reforma_do_livro())
    print(livro1.capa_dura())
    livro1.passar_paginas(111)
    print(f"Numero de paginas lidas: {livro1.paginas}")
    print(livro1.chegou_no_final(livro1.paginas))


def main():
    print("=== Demo de moeda ===")
    demo_moeda()
    print("\n=== Demo de livro ===")
    demo_livro()


if __name__ == "__main__":
    main()

