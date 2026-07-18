from datetime import date
idade_atual = str(input('Informe o ano de nascimento do jovem: '))
idade = date.today().year - int(idade_atual)
if idade == 18:
    print(f'tu ainda tens {idade} anos= {18 - idade} anos para o alistamento')
elif idade > 18:
    print(f'tu ja tens {idade} anos, ja passou {idade - 18} anos do alistamento')
    ano = date.today().year + (18 - idade)
    print(f'tu deverias ter se alistado em {ano}')
elif idade < 18:
    print(f'tu ainda deves preencher alguns anos= {18 - idade} anos para o alistamento')
    ano = date.today().year + (18 - idade)