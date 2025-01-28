tries = 0
guess = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))

print("You got it!")