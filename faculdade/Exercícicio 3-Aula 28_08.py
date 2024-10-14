# - Projete o programa que calcule as raízes de uma equação do 2° grau, levando em consideração a análise da existência de raízes reais. Se o valor de delta for menor que zero, não existem raízes nos reais; se delta for igual a zero, existem duas raízes iguais; se delta for maior que zero, existem duas raízes diferentes.
#Expressão: ax^2 + bx + c = 0
#x = - b +-  raiz_quadrada ( b^2 - 4 a c )                 delta = b^2 - 4 a c
#                         2a

import math

valor_a = float(input("Insira o valor de A: "))
valor_b = float(input("Insira o valor de B: "))
valor_c = float(input("Insira o valo de C: "))

valor_delta = valor_b**2 - 4*valor_a*valor_c
print("O valor de Delta é: ", valor_delta)

if valor_a == 0:
    print("NÃO PODE DIVIDIR POR ZERO")
elif valor_delta == 0:
    valor_x1 = ((-valor_b)+math.sqrt(valor_delta))/2*valor_a
    print("AS RAÍZES SÃO IGUAIS: x = ", valor_x1)
elif valor_delta > 0:
    valor_x1 = ((-valor_b)+math.sqrt(valor_delta))/2*valor_a
    valor_x2 = ((-valor_b)-math.sqrt(valor_delta))/2*valor_a
    print("O valor de x1 é de: ", valor_x1)
    print("O valor de x2 é de: ", valor_x2)
    print("AS RAÍZES SÃO DIFERENTES")
else:
    print("NÃO POSSUI RAÍZES")