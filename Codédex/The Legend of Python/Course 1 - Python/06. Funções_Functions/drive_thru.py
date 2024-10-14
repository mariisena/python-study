# Write code below 💖

def get_item(x):
  if x == 1:
    print('🍔 Cheeseburger')
  elif x == 2:
    print('🍟 Fries')
  elif x == 3:
    print('🥤 Soda')
  elif x == 4:
    print('🍦 Ice Cream')
  else:
    print('🍪 Cookie')

def welcome():
  print("Seja bem-vindo ao menu online")

welcome()

    
option = int(input('o que você gostaria de pedir? '))
item_escolhido = get_item(option)