ions = [
    {"nome": "Hidrogênio", "simbolo": "H+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Lítio", "simbolo": "Li+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Sódio", "simbolo": "Na+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Potássio", "simbolo": "K+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Rubídio", "simbolo": "Rb+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Césio", "simbolo": "Cs+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Magnésio", "simbolo": "Mg2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Cálcio", "simbolo": "Ca2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Estrôncio", "simbolo": "Sr2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Bário", "simbolo": "Ba2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Alumínio", "simbolo": "Al3+", "valencia": 3, "carga": "+3", "tipo": "Cátion"},
    {"nome": "Amônio", "simbolo": "NH4+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Ferro II", "simbolo": "Fe2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Ferro III", "simbolo": "Fe3+", "valencia": 3, "carga": "+3", "tipo": "Cátion"},
    {"nome": "Cobre I", "simbolo": "Cu+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Cobre II", "simbolo": "Cu2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Zinco", "simbolo": "Zn2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Prata", "simbolo": "Ag+", "valencia": 1, "carga": "+1", "tipo": "Cátion"},
    {"nome": "Chumbo II", "simbolo": "Pb2+", "valencia": 2, "carga": "+2", "tipo": "Cátion"},
    {"nome": "Sério II", "simbolo": "Ce3+", "valencia": 3, "carga": "+3", "tipo": "Cátion"},
    {"nome": "Fluoreto", "simbolo": "F-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Cloreto", "simbolo": "Cl-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Brometo", "simbolo": "Br-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Iodeto", "simbolo": "I-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Óxido", "simbolo": "O2-", "valencia": 2, "carga": "-2", "tipo": "Ânion"},
    {"nome": "Sulfeto", "simbolo": "S2-", "valencia": 2, "carga": "-2", "tipo": "Ânion"},
    {"nome": "Nitreto", "simbolo": "N3-", "valencia": 3, "carga": "-3", "tipo": "Ânion"},
    {"nome": "Hidróxido", "simbolo": "OH-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Nitrato", "simbolo": "NO3-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Sulfato", "simbolo": "SO4 2-", "valencia": 2, "carga": "-2", "tipo": "Ânion"},
    {"nome": "Carbonato", "simbolo": "CO3 2-", "valencia": 2, "carga": "-2", "tipo": "Ânion"},
    {"nome": "Fosfato", "simbolo": "PO4 3-", "valencia": 3, "carga": "-3", "tipo": "Ânion"},
    {"nome": "Bicarbonato", "simbolo": "HCO3-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Cianeto", "simbolo": "CN-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Permanganato", "simbolo": "MnO4-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Clorato", "simbolo": "ClO3-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Perclorato", "simbolo": "ClO4-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Sulfato de hidrogênio", "simbolo": "HSO4-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Borato", "simbolo": "BO3 3-", "valencia": 3, "carga": "-3", "tipo": "Ânion"},
    {"nome": "Di-hidrogenofosfato", "simbolo": "H2PO4-", "valencia": 1, "carga": "-1", "tipo": "Ânion"},
    {"nome": "Monohidrogenofosfato", "simbolo": "HPO4 2-", "valencia": 2, "carga": "-2", "tipo": "Ânion"},
    {"nome": "Tiossulfato", "simbolo": "S2O3 2-", "valencia": 2, "carga": "-2", "tipo": "Ânion"},
]


def mostrar_tabela():
    print("=" * 70)
    print("TABELA DE 40 ÍONS")
    print("=" * 70)
    print(f'{"Nº":<3} {"Nome":<20} {"Símbolo":<10} {"Valência":<10} {"Carga":<7} {"Tipo"}')
    print("-" * 70)
    for index, item in enumerate(ions, start=1):
        print(f'{index:<3} {item["nome"]:<20} {item["simbolo"]:<10} {item["valencia"]:<10} {item["carga"]:<7} {item["tipo"]}')


def buscar_ion(entrada):
    entrada = entrada.strip().lower()
    for item in ions:
        if entrada == item["nome"].lower() or entrada == item["simbolo"].lower():
            print(f'Íon encontrado: {item["nome"]} ({item["simbolo"]}) - Carga: {item["carga"]}, Valência: {item["valencia"]}, Tipo: {item["tipo"]}')
            return item
    print("Íon não encontrado. Tente novamente com o nome ou símbolo correto.")
    return None


def filtrar_por_tipo(tipo):
    return [item for item in ions if item["tipo"].lower() == tipo.lower()]


def mostrar_detalhes(item):
    print("\n Detalhes do íon")
    print(f'Nome: {item["nome"]}')
    print(f'Símbolo: {item["simbolo"]}')
    print(f'Valência: {item["valencia"]}')
    print(f'Carga: {item["carga"]}')
    print(f'Tipo: {item["tipo"]}')


def mostrar_lista_filtrada(filtrados):
    if not filtrados:
        print("Nenhum íon encontrado para o filtro informado")
        return
    print(f"\nÍons encontrados ({len(filtrados)}):")
    for item in filtrados:
        print(f'- {item["nome"]} ({item["simbolo"]}) - {item["carga"]}')


def main():
    mostrar_tabela()
    print("\nDigite o nome ou símbolo do íon para ver os detalhes.")
    print("Digite 'positivo' para ver apenas cátions, 'negativo' para ver apenas ânions.")
    print("Digite 'sair' para encerrar.")

    while True:
        escolha = input("Sua escolha: ").strip().lower()
        if escolha in ["sair", "fim", "exit"]:
            print("Encerrando o programa.")
            break
        if escolha in ["positivo", "catio", "cátion", "catios", "cátions"]:
            filtrados = filtrar_por_tipo("Cátion")
            mostrar_lista_filtrada(filtrados)
            continue
        if escolha in ["negativo", "anion", "ânion", "anions", "ânsios"]:
            filtrados = filtrar_por_tipo("Ânion")
            mostrar_lista_filtrada(filtrados)
            continue

        resultado = buscar_ion(escolha)
        if resultado:
            mostrar_detalhes(resultado)
        

if __name__ == "__main__":
    main()