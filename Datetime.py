from datetime import date
year = int(input('Qual year pretendes verificar, coloque o 0 para verificar o year atual:')) 
if year == 0:
   print(f' O year {date.today().year}, o year e bissexto {date.today().year}')
   year = date.today().year
if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    
   print(f' O year {date.today().year}, o year e bissexto {date.today().year}')          
else:
   print(f' O year {date.today().year}, o year nao e bissexto {date.today().year}')          