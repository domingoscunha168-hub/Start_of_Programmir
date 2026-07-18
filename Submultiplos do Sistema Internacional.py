from decimal import Decimal, InvalidOperation

submultiplos_si = (
    {"prefixo": "deci", "simbolo": "d", "expoente": -1, "decimal": Decimal("0.1")},
    {"prefixo": "centi", "simbolo": "c", "expoente": -2, "decimal": Decimal("0.01")},
    {"prefixo": "mili", "simbolo": "m", "expoente": -3, "decimal": Decimal("0.001")},
    {"prefixo": "micro", "simbolo": "N", "expoente": -6, "decimal": Decimal("0.000001")},
    {"prefixo": "nano", "simbolo": "n", "expoente": -9, "decimal": Decimal("0.000000001")},
    {"prefixo": "pico", "simbolo": "P", "expoente": -12, "decimal": Decimal("0.000000000001")},
    {"prefixo": "femto", "simbolo": "f", "expoente": -15, "decimal": Decimal("0.000000000000001")},
    {"prefixo": "atto", "simbolo": "a", "expoente": -18, "decimal": Decimal("0.000000000000000001")},
    {"prefixo": "zepto", "simbolo": "z", "expoente": -21, "decimal": Decimal("0.000000000000000000001")},
    {"prefixo": "yocto", "simbolo": "y", "expoente": -24, "decimal": Decimal("0.000000000000000000000001")},
)


def mostrar_tabela():
    print("=" * 20)
    print("SUBMÚLTIPLOS DO SI")
    print("=" * 20)
    print(f'{"Prefixo":<12}{"Simbolo":<10}{"Expoente":<10}{"Equivalente decimal"}')
    for item in submultiplos_si:
        print(f'{item["prefixo"]:<12}{item["simbolo"]:<10}10^{item["expoente"]:<8}{item["decimal"]}')


def localizar_submultiplo(valor_digitado):
    for item in submultiplos_si:
        if valor_digitado == str(item["expoente"]):
            return item

        try:
            if Decimal(valor_digitado) == item["decimal"]:
                return item
        except InvalidOperation:
            continue

    return None


mostrar_tabela()

valor = input("Digite o expoente (ex: -3) ou o valor decimal (ex: 0.001): ").strip().replace(",", ".")
resultado = localizar_submultiplo(valor)

if resultado:
    print("\n=== Resultado ===")
    print(f'Prefixo: {resultado["prefixo"]}')
    print(f'Simbolo: {resultado["simbolo"]}')
    print(f'Equivalente decimal: {resultado["decimal"]}')
    print(f'Expoente: 10^{resultado["expoente"]}')
else:
    print("\nNumero nao encontrado na tabela do SI.")
