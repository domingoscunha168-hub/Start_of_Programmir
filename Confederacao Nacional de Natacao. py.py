from datetime import date

atleta = int(input('Infome o ano de nascimento:' ))
idade = date.today().year - int(atleta)
print(f' o atleta tem {idade} anos')

if idade == 9:
    print(f' O atleta = {idade} e de first categoria')
elif idade <= 14:
    print(f' O atleta = {idade} e de second categoria')
elif idade <= 19:
    print(f' O atleta = {idade} e de third catgoria')
elif idade <= 25:
    print(f' O atleta = {idade} e de fourth categoria')
elif idade > 25:
    print(f' O atleta = {idade} e de fifth categoria')