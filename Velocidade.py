velocidade= float(input('Qual e a velocidade do car?'))
if velocidade > 80:
    if velocidade == 100:
        print(f' A  tua multa de R$ 200.00= {velocidade-80}')
    else:
        print(f' A  tua multa de R$ 500.00= {velocidade-100}')