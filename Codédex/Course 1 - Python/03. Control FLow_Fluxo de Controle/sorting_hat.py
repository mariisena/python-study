pontos_grifinoria = 0
pontos_corvinal = 0
pontos_lufa_lufa = 0
pontos_sonserina = 0

print('Bem-vindo ao Chapéu Seletor de Hogwarts:')
print()
print('Será que você é de qual casa de Hogwarts é:\n🦁 Grifinória\n🦅 Corvinal\n🦡 Lufa-Lufa\n🐍 Sonserina')
print()
resposta1 = int(input("Você gosta do amanhecer ou crespúsculo?\n[1] Amanhecer\n[2] Crepúsculo\nEscolha:  "))
if resposta1 == 1:
  pontos_grifinoria += 1
elif resposta1 == 2:
  pontos_corvinal += 1
else:
  print('Entrada errada')
print()
resposta2 = int(input('Quando eu morrer, quero que as pessoas se lembre de mim: \n[1] O Bom\n[2] O Grande\n[3] O Sábio\n[4] O Ousado\nEscolha:  '))
if resposta2 == 1:
  pontos_lufa_lufa += 2
elif resposta2 == 2:
  pontos_sonserina += 2
elif resposta2 == 3:
  pontos_corvinal += 2
elif resposta2 == 4:
  pontos_grifinoria +=2
else:
  print('Entrada errada')
print()
resposta3 = int(input("Qual tipo de instrumento te agrada mais?\n[1] Violino\n[2] Trompeta\n[3] Piano\n[4] Bateria\nEscolha: "))
if resposta3 == 1:
  pontos_sonserina += 4
elif resposta3 == 2:
  pontos_lufa_lufa += 4
elif resposta3 == 3:
  pontos_corvinal += 4
elif resposta3 == 4:
  pontos_grifinoria += 4
else:
  print('Entrada errada')
print()
print('Quantidade de pontos em cada casa')
print("Grifinória: ",pontos_grifinoria)
print("Cornival: ", pontos_corvinal)
print("Lufa Lufa: ", pontos_lufa_lufa)
print("Sonserina: ", pontos_sonserina)
print()
maior_pontuacao = max(pontos_grifinoria, pontos_corvinal, pontos_lufa_lufa, pontos_sonserina)

if maior_pontuacao == pontos_grifinoria:
  print("Você foi selecionado para 🦁 Grifinória!")
elif maior_pontuacao == pontos_corvinal:
  print("Você foi selecionado para 🦅 Corvinal!")
elif maior_pontuacao == pontos_lufa_lufa:
  print("Você foi selecionado para 🦡 Lufa-Lufa!")
else:
  print("Você foi selecionado para 🐍 Sonserina!")