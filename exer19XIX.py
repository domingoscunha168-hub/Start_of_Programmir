from projeto_publico.livro import Livro, livro


def main():
    livro1 = Livro("completo", "duravel", 0)
    print(livro1.reforma_do_livro())
    print(livro1.capa_dura())
    livro1.passar_paginas(9)
    livro1.passar_paginas(30)
    livro1.passar_paginas(61)
    print(f"Numero de paginas lidas: {livro1.paginas}")
    print(livro1.chegou_no_final(111))


if __name__ == "__main__":
    main()
