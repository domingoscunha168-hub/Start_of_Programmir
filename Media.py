nota_1 = float(input('Primeira nota do aluno: '))
nota_2 = float(input('Segunda nota do aluno: '))
print(f'As notas do aluno são: {nota_1} e {nota_2}')
media = (nota_1 + nota_2) / 2
if media < 10.0:
    print(f'O aluno foi reprovado com a media= {media:.1f}')
elif media >= 9.1 and media < 10.0:
    print(f'O aluno ficou de recuperacao com media= {media:.1f}')
else:
    print(f'O aluno foi aprovado com media= {media:.1f}')
    