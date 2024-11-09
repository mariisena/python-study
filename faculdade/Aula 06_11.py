lista = []
print("Digite [0] para sair")
while True:
    valores = int(input("Digite os valores: "))
    if valores == 0:
        break
    lista.append(valores)
print('lista =', lista)
qtd = len(lista)
print("Quantidade de números:", qtd)
soma = sum(lista)
print("Soma dos números:", soma)
maior_valor = max(lista)
print("Maior número:", maior_valor)
menor_valor = min(lista)
print("Menor número:", menor_valor)
pesquisa = int(input("Valor da pesquisa: "))
if 3 in lista:
    print("valor encontrado")
else:
    print("valor não encontrado")
print("ordem crescente:", sorted(lista))
lista.insert(1, 33)
print(lista)

