#1- Elabore o programa que selecione o maior valor de três valores fornecidos pelo usuário. Resolva sem usar operador lógico (e, ou, não).
def Exercício1():
    num1 = int(input("Digite valor numerico 1: "))
    num2 = int(input("Digite valor numerico 2: "))
    num3 = int(input("Digite valor numerico 3: "))
    if num1 > num2 > num3:
        print("O maior número é o: ", num1)
    elif num1 > num3 > num2:
        print("O maior número é: ", num1)
    elif num2 > num1 > num3:
        print("O maior número é: ", num2)
    elif num2 > num3 > num1:
        print("O maior número é: ", num2)
    elif num3 > num1 > num2:
        print ("O maior número é: ", num3)
    else:
        print ("O maior número é: ", num3)
# 2- Refaça o exercício anterior utilizando também operador lógico (e, ou, não).
def Exercício2():
    num1 = int(input("Digite valor numerico 1: "))
    num2 = int(input("Digite valor numerico 2: "))
    num3 = int(input("Digite valor numerico 3: "))
    if num1 > num2 and num1 > num3:
        print("O maior número é o: ", num1)
    elif num2 > num1 and num2 > num3:
        print("O maior número é: ", num2)
    else:
        print ("O maior número é: ", num3)
# 3- Elabore o programa que simule a CALCULADORA com as quatro operações aritméticas básicas. O usuário fornecerá dois números e a operação aritmética desejada. Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado.
def Exercício3():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))
    soma = num_1+num_2
    subtração = num_1-num_2
    multiplicação = num_1*num_2
    divisão = num_1/num_2
    print("Seleciona a operação:\n1) soma\n2) subtração\n3) multiplicação\n4) divisão")
    escolha = int(input("Escolha o Exercício: "))
    if escolha == 1:
        print("O valor é de: ", soma)
    elif escolha == 2:
        print("O valor é de: ", subtração)
    elif escolha == 3:
        print("O valor é de: ", multiplicação)
    else:
        print("O valor é de: ", divisão)

print("Seleciona o exercício:\n1) Exercício1\n2) Exercício2\n3) Exercício3")
escolha = int(input("Escolha o Exercício: "))
if escolha == 1:
    Exercício1()
elif escolha == 2:
    Exercício2()
else:
    Exercício3()