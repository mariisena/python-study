def Exercicio51():
    #Modifique o programa para exibir os números de 1 a 100.
    x = 1
    while x <= 100:
        print(x)
        x = x + 1

def Exercicio52():
    # Modifique o programa para exibir os números de 50 a 100
    x = 50
    while x <= 100:
        print(x)
        x = x + 1

def Exercicio53():
    # Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8..., 1, 0 e Fogo!
    x = 10
    while x >= 0:
        print(x)
        x = x - 1
    print("FOGO!")
def Exercicio54():
    #Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas dessa vez, apenas os número ímpares.
    Fim = int(input("Digite o último número fim: "))    # Resolução livro:
    x = 1                                               # x = 1
    while x <= Fim:                                     # while x <= Fim:
        if x % 2 != 0:                                  #    print(x)
            print(x)                                    #    x = x + 2
        x = x + 1
def Exercicio55():
    # Escrever os 10 primeiros múltiplos de 3
    fim = 30
    x = 3
    while x <= fim:
        print(x)
        x = x + 3
def Exercicio56():
    #Tabuada de multiplicação de 2.
    n = int(input("Tabuada de: "))
    x = 1
    while x <= 10:
        print(f"{n} x {x} = {n * x}")
        x = x + 1
def Exercicio57():
    # Usuário digite inicio e fim da tabuada de 2.
    n = int(input("Tabuada de: "))
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número fim: "))
    x = inicio
    while x < fim:
        print(f"{n} x {x} = {n * x}")
        x = x + 1
Exercicio57()