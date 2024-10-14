#exercício 1
valor_base = int(input("digite o valor da base"))
valor_altura = int(input("digite o valor da altura"))
area = valor_base*valor_altura/2
print("A área é igual a", area)

#exercício 2
base2 = float(input("digite a base: "))
altura2 = float(input("digite a altura: "))
area2 = base2*altura2/2
print("Área:", area2)
print("base:", base2)
print("altura:", altura2)
print(f"Área: {area2:.3f}")

#exercício 3
Valor_nota_1 = float(input("Digite nota 1:"))
Valor_nota_2 = float(input("Digite nota 2:"))
Média = (Valor_nota_1+Valor_nota_2)/2
print("A média é igual a:", Média)

#exercicio 4
valor_F = float(input("digite o valor da tempo:"))
Celsius = (5*(valor_F-32))/9
print(f"O valor em Celsius é igual a: {Celsius:.2f}")

#exercicio 5
valorPI = 3.14
valorRaio = float(input("Digite o valor da raio:" ))
area = valorPI*pow(valorRaio, 2)
print(f"Area é igual a: {area:.2f}")