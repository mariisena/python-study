'''Construa o programa que encontre o menor valor e maior valor de um conjunto de valores inteiros digitados em conjunto de valores inteiros digitados pelo usuário. A condição de saída será o valor 0 (zero) que não será considerado na pesquisa.'''

menor_valor = float('inf')                              #9999999
maior_valor = float('-inf')                             #-9999999
ct = 0
soma = 0
print("Digite 0 para saída")

while True:                                             # while valor != -1
    valor = int(input("Digite um número: "))
    if valor == 0:
        break
    ct = ct + 1
    soma = soma + valor
    if valor < menor_valor:                             
        menor_valor = valor                             # Se for menor, atualize o valor da variável menor.
    if valor > maior_valor:                             # Aqui não pode else
        maior_valor = valor
    media = soma / ct
    # Fim da repetição while
print("Quantidade de valores digitados: ", ct)
print("Soma do valores digitados: ", soma)
print("A média é de: ", media)
print("O maior valor é: ", maior_valor)
print("O menor valor é: ", menor_valor)

'''Elabore o programa que leia a altura e o gênero ('m' para masculino e 'f' para feminino) de um grupo de pessoas. Gere a tela de saída com as seguintes informações: maior altura do grupo (de todas as pessas), menor altura do grupo (de todas as pessoas), quantidade de homens e quantidade de mulheres.'''
'''Elabore o programa que leia a altura e o gênero ('m' para masculino e 'f' para feminino) de um grupo de pessoas. Gere a tela de saída com as seguintes informações: maior altura do grupo (de todas as pessas), menor altura do grupo (de todas as pessoas), quantidade de homens e quantidade de mulheres.'''

maior_altura = float('-inf')
menor_altura = float('inf')
ct_masculino = 0
ct_feminino = 0
print("Digite 0 para sair: ")

while True:
    altura = float(input("Digite sua altura: ")) 
    if altura == 0:
        break
    genero = str(input("Digite a sua genero:\n[m] masculino\n[f] feminino\nescolha a opção: "))
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    if genero == 'm':
        ct_masculino = ct_masculino + 1
    else:
        ct_feminino = ct_feminino + 1
print("Menor altura é: ", menor_altura)
print("Maior altura é: ", maior_altura)
print("Quantidade de homens: ", ct_masculino)
print("Quantidade de mulheres: ", ct_feminino)

