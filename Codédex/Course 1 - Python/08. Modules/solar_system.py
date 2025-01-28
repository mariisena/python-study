from random import choice as ch
from math import pi

planets = [
  'Mercúrio',
  'Venus',
  'Terra',
  'Marte',
  'Saturno'
]

random_planet = ch(planets)
if random_planet == 'Mercúrio':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Terra':
    r = 6371
elif random_planet == 'Marte':
    r = 3390
elif random_planet == 'Saturno':
    r = 58232
else:
    print('Oops! Um erro occoreu!')

if r is not None:
    area = 4 * pi * r**2
    print(f"O planeta é {random_planet}, e sua área de superfície é de aproximadamente {area:,.2f} quilômetros quadrados.")