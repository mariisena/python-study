earth_weight = float(input("Seu peso na Terra: "))
planet = int(input("Número do planeta (1-7): "))
if planet == 1:
  relative_gravity = 0.38
  destination_weight = earth_weight * relative_gravity
  print("Mercury: ", destination_weight)
elif planet == 2:
  relative_gravity = 0.91
  destination_weight = earth_weight * relative_gravity
  print("Venus: ", destination_weight)
elif planet == 3:
  relative_gravity = 0.38
  destination_weight = earth_weight * relative_gravity
  print("Mars: ", destination_weight)
elif planet == 4:
  relative_gravity = 2.53
  destination_weight = earth_weight * relative_gravity
  print("Jupiter: ", destination_weight)
elif planet == 5:
  relative_gravity = 1.07
  destination_weight = earth_weight * relative_gravity
  print("Saturn: ", destination_weight)
elif planet == 6:
  relative_gravity = 0.89
  destination_weight = earth_weight * relative_gravity
  print("Uranus: ", destination_weight)
elif planet == 7:
  relative_gravity = 1.14
  destination_weight = earth_weight * relative_gravity
  print("Neptune: ", destination_weight)
else:
  print('Invalid planet number')