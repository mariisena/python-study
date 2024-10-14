# Recebe um número digitado
valor = int(input("Digite um número: "))
# Verifica se valor >= 100 para mostrar a mensagem
if valor >= 100:                            # Obrigatório usar os dois pontos [:]
    print("Valor maior ou igual a cem.")    # Indentação (to ident) obrigatória
else:                                       # Caso não seja verdade
    print("valor menor que cem.")

#EXERCÍCIO 1
nota_1 = float(input("Valor da nota 1: "))
nota_2 = float(input("Valor da nota 2: "))
media = (nota_1+nota_2)/2
print(f"Média = {media:.2f}")
if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")

#EXERCÍCIO 2
valor = int(input("Valor do número 1: "))
resto = valor%2
print("Valor igual a:", resto)
if resto == 0:
    print("Número par")
else:
    print("Número impar")

#Solução 2 para o exercício 2
valor = int(input("Digite um número:"))
if valor %2 == 0:
    print(f"O número {valor} é par")
else:
    print(f"O número {valor} é impar")
#EXERCÍCIO 3
senha = int(input("DIGITE SUA SENHA: "))
if senha == 123:
    print("SENHA CORRETA")
else:
    print("SENHA ERRADA")

#EXERCÍCIO 4
valor = float(input("DIGITE UM NÚMERO: "))
if valor == 0:
    print("NULO")
elif valor < 0:
    print("NEGATIVO")
else:
    print("POSITIVO")

#EXERCÍCIO 5
valor = float(input("DIGITE UM NÚMERO: "))
print("Número:", valor)
if valor == 0:
    print("NULO")
elif valor < 0:
    print("NEGATIVO")
else:
    print("POSITIVO")
    print("dobro do número:", valor*2)

#EXERCÍCIO 6: Construa um programa que leia dois valores quaisquer
#e mostre o maior deles ou mestre a mensagem "os valores são iguais"

valor_1 = float(input("Digite valor 1: "))
valor_2 = float(input("Digite valor 2: "))
if valor_1 > valor_2:
    print("O maior valor é:", valor_1)
elif valor_2 > valor_1:
    print("O maior valor é>", valor_2)
else:
    print("Os valores são iguais.")