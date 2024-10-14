#Implemente o programa que gere a sequência dos números naturais na ordem crescente até um valor final fornecido pelo usuário. Mostre também a quantidade de valores da sequência gerada. 
def Exercicio1 ():
    num1 = int(input("Digite número inicial: "))
    num2 = int(input("Digite número final: "))
    ct = 0
    for sequencia in range (num1,num2+1):
      if sequencia:
        print(sequencia)
        ct = ct + 1
    print("Quantidade de números: ", ct)
           
#Elabore o programa que gere a sequência do dobro dos números naturais até dez na ordem crescente. Mostre também a soma e a média aritmética da sequência gerada. Use for.
def Exercicio2():
    soma = 0
    for i in range(1,11):
      dobro = i * 2
      print(dobro)
      soma = soma + i
      media = soma/10
    print("A soma é de: ", soma)
    print("A média é de: ", media) 

#Refaça o programa que calcule a média aritmética de uma turma com cinquenta alunos. Onde cada aluno realizou uma avaliação.
#Observação: para facilitar os testes na implementação, troque o valor cinquenta por cinco.
def Exercicio3 ():
    total_notas = 0
    num_alunos = int(input("Quantidade de alunos: "))
    for i in range(1,num_alunos+1):
       notas = float(input("Digite a nota: "))
       total_notas = total_notas + notas
    media = total_notas/num_alunos
    print("A média dos alunos é de: ", media)

#A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo. Calcule a conversão e construa o relatório de saída tabular (em forma de tabela de duas colunas) de graus Celsius em função de graus Fahrenheit que que variam de 45 a 80 de 1 em 1. Fórmula: c = 5 ( f - 32 )/9
def Exercicio4 ():
   print(f"{"Fahreinheit"} | {"Celsius"}")
   for f in range(45,81):
      valor_celsius = 5 * (f - 32)/9
      print(f"{f:.1f} ºF | {valor_celsius:.3f} ºC")

#Construa o programa que gere cinco números inteiros aleatórios sorteados pelo computador. Eles devem estar no intervalo fechado de zero a noventa e cinco.
def Exercicio5 ():
   import random

   numero_sorteado = random.randint(0,96)
   print("O número sorteado é: ", numero_sorteado)

Exercicio5 ()