import math 
valor_x1 = float(input("Digite valor de x1: ")) 
valor_y1 = float(input("Digite valor de y1: ")) 
valor_x2 = float(input("Digite valor de x2: ")) 
valor_y2 = float(input("Digite valor de y2: ")) 
print("P = ", valor_x1,",",valor_y1) 
print("Q = ", valor_x2,",", valor_y2) 
distancia = math.sqrt((valor_x2 - valor_x1)**2 + (valor_y2 - valor_y1)**2) 
print(f"A distância é de: {distancia:.2f}")