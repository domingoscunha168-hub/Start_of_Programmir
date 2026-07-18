numero = int(input('first valor:'))
numero_2 = int(input(' second valor:'))
numero_3 = int(input('trety valor:'))


if numero < numero_2 and numero < numero_3:
    menor = numero
elif numero_2 < numero and numero_2 < numero_3:
    menor = numero_2
else:
    menor = numero_3

if numero > numero_2 and numero > numero_3:
    maior = numero
elif numero_2 > numero and numero_2 >numero_3:
    maior = numero_2
else:
    maior = numero_3

print(f'O valor menor digitado entre  ({numero}, {numero_2} e {numero_3} é {menor}), e o valor maior digitado entre ({numero}, {numero_2} e {numero_3} é {maior})')           
    
   