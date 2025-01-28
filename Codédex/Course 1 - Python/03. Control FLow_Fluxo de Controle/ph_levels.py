print("De 0 a 14, qual o pH?")
valor_ph = float(input("Valor pH: "))
if valor_ph > 7:
  print('BÁSICO')
elif valor_ph < 7:
  print('ÁCIDA')
else:
  print('NEUTRO')