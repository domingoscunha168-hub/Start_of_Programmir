def ler_medida():
    return float(input('Informe a distancia:'))

medida = ler_medida()
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
hm = medida / 100
dam = medida / 10
if medida != 9:
      print(' A media é diferente de 9')    
print('=== Conversao de Medidas ===')
print(f' A medida = {medida:.3f}\n Em centimetros é equivalente a {cm:.3f}\n Em milimetros é equivalente a {mm:.3f}\n Em decimetros é equivalente a {dm:.3f}\n Em quilometros é equivalente a {km:.3f}\n Em hectometros é equivalente a {hm:.3f}\n Em decametros é equivalente a {dam:.3f}')