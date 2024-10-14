ct = 0
soma = 0                                                  # Valor inicial da variável
print("Digite [-1] para sair")
while True:                                             # Laço de repetição, repere enquanto condição verdadeira
    numero = int(input("Digite um número: "))           # Identação é obrigatória
    if numero == -1:
        break                                           # Sai de uma estrutura de repetição (while)
    ct = ct + 1                                         # ct + =1 (contador), incrementa o ct
    soma = soma + numero                                # soma +- = numero (somador ou acumulador)
    #Fim da estrutura de repetição "while"
print("Quantidade de números: ", ct)
print("Soma dos valores digitados: ", soma)

'''Passos para resolução do problema (algoritmo):
variável ct
variável soma
estrutura de repetição    
    lê nota
    teste condição saída
    contador
    somador
calcule média
tela de saída'''

'''Desenvolva o programa que calcule a média aritmética de uma turma, onde cada aluno realizou uma avaliação.
Não sabemos a quantidade de alunos, por isso usaremos o valor "-1" com condição (flag) de saída.
Na tela de saída, mostre a média aritmética da turma e a quantidade de alunos da turma.'''


ct = 0
soma = 0
print("Digite [-1] para sair")
while True:
    nota = int(input("Nota do aluno: "))
    if nota == -1:
        break
    ct = ct + 1
    soma = soma + nota
print("Quantidade de números: ", ct)
calculo_media = soma/ct
print(f"Soma dos valores digitados: {calculo_media:.2f}")

'''Construa o programa que calcule a média aritmética dos números pares.
O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou impar.
A condição de saída será o número zero (zero)'''

ct = 0
soma = 0
print("Digite o número 0 para sair")
while True:
    nota = int(input("Nota do aluno: "))
    if nota == 0:
        break
    resto = nota % 2                                    # O operador % pega o resto da divisão
    if resto % 2 == 0:                                  # Se o resto for zero 0 o valor é par
        ct = ct + 1
        soma = soma + nota
print("Quantidade de números: ", ct)
calculo_media = soma/ct
print(f"Soma dos valores digitados: {calculo_media:.4f}")

'''Construa o programa que encontre o menor valoor de um conjunto de valores inteiros digitados pelo usuário.
Na condição de saída, use o valor 0 (zero) que não será considerado na pesquisa.

- Passos para resolução do problema(algoritmos):
variável menor_valor    (inicia variável)
estrutura de repetição
    lê valor
    tenta condição saída
    compara o número lido (valor) com o menor valor
        atualiza ou não o menor valor
Tela de saída           (fim de algoritmo)

Teste 1: valor: 2, 1, 3, 0 Saída: Menor = 1
Teste 2: valor: 1, 3, 2, 0 Saída: Menor = 1
Teste 3: valor: 3, 2, 1, 0 Saída: Menor = 1
'''

menor_valor = 9999999
ct = 0
print("Digite o número 0 para saída")
while True:
    valor = int(input("Digite um número: "))
    if valor == 0:
        break
    ct = ct + 1 
    if valor < menor_valor:
        menor_valor = valor
print("O menor valor é", menor_valor)
print("Valores digitados:   ", ct )