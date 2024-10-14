# Analise o resultado de uma transação comercial. Verifique a situação final do comerciante trabalhando com os valores lidos, ou seja, o preço de compra e o preço de venda. Gere a tela de saída com uma das seguintes mensagens: "teve lucro", "teve prejuízo" ou "os valores são iguais".

valor_compra = float(input("Preço de compra: "))
valor_venda = float(input("Preço de venda: "))
if valor_compra>valor_venda:
    print("teve prejuízo")
    print(valor_compra - valor_venda)
elif valor_venda>valor_compra:
    print("teve lucro")
    print(valor_venda - valor_compra)
else:
    print("os valores são iguais")

print(f"valor da compra: {valor_compra:.0f}")
print(f"valor da venda: {valor_venda:.0f}")

valor_a = float(input("Digite valor de A: "))
valor_b = float(input("Digite valor de B: "))
if valor_a == 0:
    print("não pode dividir por zero")
else:
    X = -(valor_b)/valor_a
    print("Raiz: ", X)