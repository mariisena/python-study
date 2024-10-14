import random

def fortune():
  fortune = (random.randint(0, 7))
  if fortune == 0:
      print("Não busque a felicidade. Crie-a.")
  elif fortune == 1:
      print("All things are difficult before they are easy.")
  elif fortune == 2:
      print("O pássaro que madruga pega o verme, mas o segundo rato pega o queijo.")
  elif fortune == 3:
      print("Alguém em sua vida precisa de uma carta sua.")
  elif fortune == 4:
      print("Não pense apenas. Aja!")
  elif fortune == 5:
      print("Seu coração vai pular uma batida.")
  elif fortune == 6:
      print("A fortuna que você procura está em outro biscoito.")
  else:
      print("Socorro! Estou sendo mantido prisioneiro em uma padaria chinesa!")

fortune()