dias = int(input('Informe os dias que o carro ficou alugado:'))
km = float(input('Informe os km que foram percorridos:'))
preco = (dias*60) + (km*1.15)
print(f' O Valor a ser pago e {preco:.2f}') 