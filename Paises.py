from typing import Dict, List, Tuple
from time import sleep


continentes: Dict[str, List[str]] = {
    "África": [
        "África do Sul", "Argélia", "Angola", "Benin", "Botsuana", "Burquina Faso", "Burundi",
        "Cabo Verde", "Camarões", "Chade", "Comores", "Costa do Marfim", "Djibuti",
        "Egito", "Guiné Equatorial", "Eritreia", "Essuatíni", "Etiópia", "Gabão",
        "Gâmbia", "Gana", "Guiné", "Guiné-Bissau", "Quênia", "Lesoto", "Libéria",
        "Líbia", "Madagáscar", "Malawi", "Mali", "Mauritânia", "Maurício", "Marrocos",
        "Moçambique", "Namíbia", "Níger", "Nigéria", "República Centro-Africana",
        "República Democrática do Congo", "República do Congo", "Ruanda",
        "São Tomé e Príncipe", "Senegal", "Seicheles", "Serra Leoa", "Somália",
        "Sudão", "Sudão do Sul", "Tanzânia", "Togo", "Tunísia", "Uganda", "Zâmbia",
        "Zimbábue"
    ],
    "América do Norte": [
        "Antígua e Barbuda", "Bahamas", "Barbados", "Belize", "Canadá", "Costa Rica",
        "Cuba", "Dominica", "República Dominicana", "El Salvador", "Granada", "Guatemala",
        "Haiti", "Honduras", "Jamaica", "México", "Nicarágua", "Panamá",
        "Santa Lúcia", "São Cristóvão e Nevis", "São Vicente e Granadinas",
        "Trinidad e Tobago", "Estados Unidos"
    ],
    "América do Sul": [
        "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana",
        "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"
    ],
    "Ásia": [
        "Afeganistão", "Arábia Saudita", "Bahrein", "Bangladesh", "Butão", "Brunei",
        "Camboja", "China", "Coreia do Norte", "Coreia do Sul", "Cazaquistão",
        "Catar", "Emirados Árabes Unidos", "Filipinas", "Geórgia", "Índia", "Indonésia",
        "Irã", "Iraque", "Israel", "Japão", "Jordânia", "Quirguistão", "Kuwait",
        "Laos", "Líbano", "Malásia", "Maldivas", "Mianmar", "Mongólia", "Nepal",
        "Omã", "Paquistão", "Palestina", "Rússia", "Singapura", "Sri Lanka",
        "Síria", "Tadjiquistão", "Tailândia", "Timor-Leste", "Turcomenistão",
        "Turquia", "Uzbequistão", "Vietnã", "Iêmen"
    ],
    "Europa": [
        "Albânia", "Alemanha", "Andorra", "Armênia", "Áustria", "Azerbaijão",
        "Bélgica", "Bielorrússia", "Bósnia e Herzegovina", "Bulgária", "Chipre",
        "Croácia", "Dinamarca", "Eslováquia", "Eslovênia", "Espanha", "Estônia",
        "Finlândia", "França", "Grécia", "Hungria", "Islândia", "Irlanda", "Itália",
        "Letônia", "Liechtenstein", "Lituânia", "Luxemburgo", "Malta", "Moldávia",
        "Mônaco", "Montenegro", "Noruega", "Países Baixos", "Polônia", "Portugal",
        "Reino Unido", "Romênia", "Sérvia", "Suécia", "Suíça", "Ucrânia",
        "Vaticano"
    ],
    "Oceania": [
        "Austrália", "Fiji", "Ilhas Marshall", "Ilhas Salomão", "Kiribati", "Micronésia",
        "Nauru", "Nova Zelândia", "Palau", "Papua-Nova Guiné", "Samoa", "Tonga",
        "Tuvalu", "Vanuatu"
    ],
}


def listar_continentes() -> List[str]:
    return sorted(continentes.keys())


def buscar_continentes_por_letra(letra: str) -> List[str]:
    letra = letra.upper()
    return sorted([continente for continente in continentes if continente.upper().startswith(letra)])


def listar_paises_por_continente(continente: str) -> List[str]:
    return sorted(continentes.get(continente, []))


def buscar_paises_por_letra(letra: str) -> List[Tuple[str, str]]:
    letra = letra.upper()
    resultados: List[Tuple[str, str]] = []
    for continente, paises in continentes.items():
        for pais in paises:
            if pais.upper().startswith(letra):
                resultados.append((pais, continente))
    return sorted(resultados, key=lambda item: item[0].upper())


def mostrar_continente(continente: str) -> None:
    print(f"\n{continente.upper()}")
    print("-" * len(continente))
    for pais in listar_paises_por_continente(continente):
        print(f"• {pais}")
    sleep(0.4)


def mostrar_paises_por_letra(letra: str) -> None:
    resultados = buscar_paises_por_letra(letra)
    if resultados:
        print(f"\nPaíses que começam com '{letra}':")
        for pais, continente in resultados:
            print(f"• {pais} — esse país é do continente {continente}.")
    else:
        print(f"\nNenhum país encontrado com a letra '{letra}'.")


def main() -> None:
    print("=== CATÁLOGO DE CONTINENTES E PAÍSES ===")
    print("Continentes disponíveis:", ", ".join(listar_continentes()))
    print("Digite uma letra para ver os continentes e os países que começam com ela.")
    print("Exemplo: A, E, O, S ou 0 para sair.")

    while True:
        opcao = input("\nDigite uma letra: ").strip()

        if not opcao:
            print("Digite uma letra válida.")
            continue

        if opcao.upper() in {"0", "SAIR", "S"}:
            print("Encerrando o programa...")
            break

        if len(opcao) != 1 or not opcao.isalpha():
            print("Digite apenas uma letra.")
            continue

        letra = opcao.upper()

        continentes_encontrados = buscar_continentes_por_letra(letra)
        if continentes_encontrados:
            print(f"\nContinentes que começam com '{letra}':")
            for continente in continentes_encontrados:
                print(f"• {continente}")
        else:
            print(f"Nenhum continente encontrado com a letra '{letra}'.")

        mostrar_paises_por_letra(letra)
        sleep(0.4)


if __name__ == "__main__":
    main()