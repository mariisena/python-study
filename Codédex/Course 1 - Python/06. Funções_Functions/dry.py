#lista
numeros = [10, 20, 589, 2547, 621, 14, 4761, 750]

#exibir informações na tela e facilitar a compreensão do código
print(numeros)

#len() → Devolve o comprimento (o número de itens) de um objeto
print(len(numeros))

#hasattr() → ferramenta útil para determinar se um objeto possui um atributo específico
if hasattr(numeros, "14"):
  print("A pessoa tem o atributo '14'.")
else:
  print("A pessoa não tem o atributo '14'.")

#permite que voê colete infos do seu usuário durante a execução do programa
nome = input('digita qualquer coisa: ')
print(nome)

#Retorna um número de ponto flutuante construído a partir de um número ou string
float('+1.23')