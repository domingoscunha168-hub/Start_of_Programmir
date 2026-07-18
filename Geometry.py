from math import sin, cos
hipotenusa = int(input('Digite o valor da hipotenusa: '))
angulo = float(input('Dgite o valor do angulo em graus:'))
angulo_rad = angulo * (3.14159 / 180)
cateto_oposto = sin(angulo_rad) * hipotenusa
cateto_adjacente = cos(angulo_rad) * hipotenusa
print(f'O cateto oposto e {cateto_oposto:.2f} e o cateto adjacente e {cateto_adjacente:.2f}')
if hipotenusa == 0:
    print('O valor da hipotenusa e neutro')
elif hipotenusa > 0:
    print('O valor da hipotenusa e positivo')
    while True:
        angulo = float(input('Digite o valor do angulo em graus:'))
        if angulo < 0 or angulo > 90:
            print('O valor do angulo deve estar entre 0 e 90 graus')
        else:
            break