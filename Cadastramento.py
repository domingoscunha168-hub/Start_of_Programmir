maiores_18 = 0
homens = 0
mulheres_menores_20 = 0

while True:
    try:
        idade = int(input('Informe a idade: ').strip())
    except ValueError:
        print('Incorreto. Informe o valor inteiro para a idade')
        continue

    genero = input('Informe o genero [M/F]: ').strip().upper()
    if genero not in ('M', 'F'):
        print('Incorreto. Use M para masculino ou F para feminino')
        continue

    if idade > 18:
        maiores_18 += 1
    if genero == 'M':
        homens += 1
    if genero == 'F' and idade < 20:
        mulheres_menores_20 += 1

    apoio = input('Deseja continuar? [S/N]: ').strip().upper()
    if apoio != 'S':
        break

print(' \nResultado do cadastro:')
print(f' As Pessoas com mais de 18 anos= {maiores_18}')
print(f' Os Homens cadastrados= {homens}')
print(f' As Mulheres com menos de 20 anos= {mulheres_menores_20}')
