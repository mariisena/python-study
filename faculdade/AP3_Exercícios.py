def Exercício1():
    '''1. Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações: A quantidade de valores digitados; A soma dos valores digitados; A média aritmética dos valores digitados; E a quantidade de valores digitados maior que 20.'''

    numero = 1
    soma = 0
    ct = 0
    maiores_que_20 = 0
    print("Digite [-1] para sair")

    while True:
        numero = int(input("Digite um número: "))
        if numero < 0:
            break
        soma = soma + numero
        ct = ct + 1
        if numero > 20:
            maiores_que_20 += 1

    # Calculando a média
    media = soma / ct

    # Imprimindo os resultados
    print("Quantidade de valores digitados:", ct)
    print("Soma dos valores:", soma)
    print(f"Média aritmética: {media:.2f}")
    print("Quantidade de valores maiores que 20:", maiores_que_20)

def Exercício2():
    '''2. Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com as seguintes informações: a quantidade de alunos aprovados, a quantidade de alunos reprovados e a quantidade de alunos que fizeram a prova. Considere que o aluno será aprovado com nota for maior ou igual a cinco.'''

    aprovados = 0
    reprovados = 0
    total_alunos = 0
    print("Digite -1 para sair")
    while True:
        nota = float(input("Digita a nota do aluno: "))
        
        if nota < 0:
            break
        total_alunos = aprovados + reprovados
        if nota >= 5:
            aprovados = aprovados + 1
        else:
            reprovados = reprovados + 1
    print("Total de alunos: ", total_alunos)
    print("Alunos aprovados: ", aprovados)
    print("Alunos reprovados: ", reprovados)

def Exercício3():
    '''3. Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos números ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar. A condição de saída será o número 0 (zero).'''
    soma_pares = 0
    soma_impares = 0
    ct_pares = 0
    ct_impares = 0
    print("Digite 0 [ZERO] para sair")

    while True:
        numero = int(input("Digite um número: "))

        if numero == 0:
            break

        if numero % 2 == 0:
            soma_pares = soma_pares + numero
            ct_pares = ct_pares + 1
        else:
            soma_impares = soma_impares + numero
            ct_impares = ct_impares + 1

    if ct_pares > 0:
        media_pares = soma_pares / ct_pares
        print("Média dos números pares:", media_pares)
    else:
        print("Não foram digitados números pares.")

    if ct_impares > 0:
        media_impares = soma_impares / ct_impares
        print("Média dos números ímpares:", media_impares)
    else:
        print("Não foram digitados números ímpares.")

print("Seleciona o exercício:\n1) Exercício1\n2) Exercício2\n3) Exercício3")
escolha = int(input("Escolha o Exercício: "))
if escolha == 1:
    Exercício1()
elif escolha == 2:
    Exercício2()
else:
    Exercício3()