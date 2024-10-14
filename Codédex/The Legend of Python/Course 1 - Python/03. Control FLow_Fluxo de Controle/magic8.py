import random
question = input('Pergunta: ')
num = random.randint(1, 9)
if num == 1:
    print('Magic 8 ball: Sim!')
elif num == 2:
    print('Magic 8 ball: Claro que sim!')
elif num == 3:
    print('Magic 8 ball: Sem dúvida!')
elif num == 4:
    print('Magic 8 ball: Resposta nebulosa, tente novamente!')
elif num == 5:
    print('Magic 8 ball: Pergunte novamente mais tarde!')
elif num == 6:
    print('Magic 8 ball: Melhor não contar agora!')
elif num == 7:
    print('Magic 8 ball: Minhas fontes dizem que não')
elif num == 8:
    print('Magic 8 ball: Perpectiva não tão boa.')
else:
    print('Magic 8 ball: Muito duvidoso.')

#resolução codédex
'''import random

question = input('Question:      ')

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Magic 8 Ball:  ' + answer)'''