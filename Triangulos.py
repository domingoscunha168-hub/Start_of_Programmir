t_1 = float(input('first segment'))
t_2 = float(input('second segment'))
t_3 = float(input('third segment'))
if t_1 < t_2 + t_3 and t_2 < t_1 + t_3 and t_3 < t_1 + t_2:
    print(f' Os segmentos {t_1}, {t_2} e {t_3} podem formar um triangulo?')
if t_1 == t_2 and t_2 == t_3:
    print('Equilatero')
elif t_1 == t_2 or t_2 == t_3 or t_1 == t_3:
    print('Isosceles')
else:
    print('Escaleno')

