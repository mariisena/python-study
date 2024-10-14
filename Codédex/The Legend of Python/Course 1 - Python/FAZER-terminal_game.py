# Escreva o código abaixo 💖

import random

# Title
print("===================\nRock Paper Scissors\n===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
# Variables/ inputs
player = int(input("Pick a number: "))
computer = random.randint(0,3)
# blank line
print()
if player == 1 and computer == 1:
  print("Player chose ✊")
  print("Computer chose ✊")
  print("The Player and Computer tie!")
elif player == 2 and computer == 2:
  print("Player chose ✋")
  print("Computer chose ✋")
  print("The Player and Computer tie!")
elif player == 3 and computer == 3:
  print("Player chose ✌️")
  print("Computer chose ✌️")
  print("The Player and Computer tie!")
elif player == 1 and computer == 3:
  print("Player chose ✊")
  print("Computer chose ✌️")
  print("The Player Wins! :)")
elif player == 2 and computer == 1:
  print("Player chose ✋")
  print("Computer chose ✊")
  print("The Player Wins! :)")
elif player == 3 and computer == 2:
  print("Player chose ✌️")
  print("Computer chose ✋")
  print("The Player Wins! :)")
elif player == 1 and computer == 2:
  print("Player chose ✊")
  print("Computer chose ✋")
  print("The Computer Wins! :(")
elif player == 2 and computer == 3:
  print("Player chose ✋")
  print("Computer chose ✌️")
  print("The Computer Wins! :(")
elif player == 3 and computer == 1:
  print("Player chose ✌️")
  print("Computer chose ✊")
  print("The Computer Wins! :(")
else:
  print("Number inputted is invalid")