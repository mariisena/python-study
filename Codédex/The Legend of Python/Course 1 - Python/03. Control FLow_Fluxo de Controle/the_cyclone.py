v_altura = int(input('Qual é a sua altura (cm)? '))
v_credito = int(input('Quantos créditos você tem? '))
if v_altura >= 137 and v_credito >= 10:
  print('Aproveite o passeio!')
elif v_altura <= 137 and v_credito >= 10:
  print('Você não é alto o suficiente para andar')
elif v_altura >= 137 and v_credito <= 10:
  print('Você não tem créditos suficientes')
else:
  print('Não tem altura nem crédito')