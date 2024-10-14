#Elabore o programa que gere a sequência dos números inteiros de um em um, onde o usuário fornecerá os valores inicial e final da sequência.
def Exercicio1():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    ct = 0
    soma = 0
    print("- Sequência de números inteiros: ")
    for numero in range(n1,n2+1):
      if numero:
        print(numero, end= ",")
        ct = ct + 1
        soma = numero + soma
    print("\nQuantidade de números: ", ct)
    print("A soma é de: ", soma)

# Melhore o progama anterior, se o usuário fornecer o valor inicial menor que o valor final, gera a sequência na ordem crescente. E se o valor inicial for maior que o valor final, gere a sequência na ordem decrescente.
def Exercicio2():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    ct = 0
    soma = 0
    print("- Sequência de números inteiros: ")
    if n1 <= n2:
      for numero in range(n1,n2+1,1):
        if numero == n2:
          print(numero,end= ".")
        else:
          print(numero,end=",")
        ct = ct + 1
        soma = numero + soma
    else:
      for numero in range(n1,n2-1,-1):
        if numero == n2:
          print(numero,end=".")
        else:
          print(numero,end=",")
        ct = ct + 1
        soma = numero + soma
    print("\nQuantidade de números: ", ct)
    print("A soma é de: ", soma)

# Elabore o programa para somar todos os númerps inteiros que se encontam no intervalo de um a quinhentos.
def Exercicio3():
  n1 = int(input("Primeiro numero: "))
  n2 = int(input("Segundo número: "))
  soma = 0
  for numero in range(1,501,1):
    if numero:
      print(numero)
    soma = numero + soma
  print("A soma é de: ", soma)

#Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três e que se encontram no intervalo de um a quinhentos.
def Exercicio4():
  soma = 0
  ct = 0
  for numero in range(1,501,1):
    if numero % 2 == 1:
     if numero % 3 == 0:
      soma = numero + soma
      ct = ct + 1
  print("Quantidade: ", ct)
  print("A soma é de: ", soma)

Exercicio4()