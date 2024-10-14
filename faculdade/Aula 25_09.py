#Elabore o prgorama que gere a sequência dos números naturais até 10 na vertical.
def Ex1():
    ct = 0
    print('- Números naturais na vertical:')
    for numero in range(0,11,1):
        ct = ct + 1
        print(numero)
    else:
        print('Encerrou o programa!')
    print('Quantos números contados:', ct)

#Elabore o programa que gere a sequência dos números naturais até 10 na horizontal.
def Ex2():
    print('- Números naturais na horizontal:')
    for i in range(0,10+1,1):
        if i <= 9:
            print(i, end=", ")
        else:
            print(i, end='.')
    print('\nEncerrou o programa.')

#Elabore o programa que gere a sequência dos números naturais pares até 12.
def Ex3():
    print('- Número naturais pares:')
    for par in range(0,13,2):
        print(par)
    print('\nEncerrou o programa.')

#Elabore o programa que gere a sequência dos números naturais ímpares até 13.
def Ex4():
    print('-Números ímpares:')
    for i in range(1,14,2):
        print(i)

#Elabore o programa que gere a sequência dos números naturais na ordem descrescente de 7 até 0.
def Ex5():
    soma = 0
    ct = 0
    print('Ordem descrente:')
    for i in range(7,-1,-1):
        print(i)
        ct = ct + 1
        soma = soma + i
    print('encerra o programa')
    print('A soma é de:', soma)

#Elabore o programa que gere a sequência dos números inteiros de um em um, onde o usuário fornecerá os valores inicial da sequência.
def Ex6():
    valor_inicial = int(input('Digite um número: '))
    valor_final = int(input('Digite outro número: '))
    for i in range(valor_inicial,valor_final+1,1):
        print(i)

#run
Ex6()