def desafio1():
    nome = input("Qual é o seu nome? ")
    print(f"Olá {nome}! Prazer em te conhece.")

def desafio2():
    dia = input("Dia do nascimento: ")
    mês = input("Mês do nascimento: ")
    ano = input("Ano de nascimento: ")
    print(f"Você nasceu no dia {dia} de {mês} de {ano}. Correto?")

def desafio3():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"A soma de {a} + {b} é de {a + b}")       #print('A soma vale()'.format(s))

def desafio4():
    a = input('Digite algo: ')
    print('O tipo primitivo é', type(a))
    print('Só tem espaços?', a.isspace())
    print('É um número?', a.isnumeric())
    print('É um alfabético?', a.isalpha())
    print('É alfanumérico', a.isalnum())
    print('Está em maiúsculas?', a.isupper())
    print('Está em minúsculas?', a.islower())
    print('Está capitalizada?', a.istitle())

'''Ordem de Precedência:
1 - ()
2 - **
3 - *, /, //, %
4 - +, - '''

def desafio5():
    n1 = int(input("Digite um número: "))
    print(f"Analisando o valor {n1}, seu antecessor é {n1-1} e o sucessor é {n1+1}")

def desafio6():
    import math
    n = int(input("Digite um número: "))
    print("O dobro do núemro é:", n * 2)
    print("O triplo do número é:", n * 3)
    print(f"A raiz quadrada é: {math.sqrt(n):0.2f}")          #para calcular a raíz pode usar também **(1/2)

#RUN
desafio6()