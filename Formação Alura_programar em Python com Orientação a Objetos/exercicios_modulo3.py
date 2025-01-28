def exercicio_1():
    lista_numeros = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_nomes = ["Mariana", "Samaryllene", "Evelen", "Jaqueláine"]
    lista_ano = [1993, 2025]

    print("Números: ", lista_numeros)
    print("Nomes: ", lista_nomes)
    print(f"Ano de nascimento: {lista_ano[0]} e ano atual: {lista_ano[1]}")

def exercicio_2():
    lista_frutas = ["Morango", "Maçã", "Banana", "Amora", "Kiwi", "Limão"]
    for frutas in (lista_frutas):
        print(frutas)

def exercicio_3():
    soma = 0
    lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in lista_numero:
        if x % 2 != 0:
            soma = soma + x
    print(f"A soma é de {soma}")

def exercicio_4():
    for x in range(10, 0, -1):
        print(x)

def exercicio_5():
    numero = int(input("Digite um número: "))
    for i in range(1, 11):
        resultado =  i * numero
        print(f"{i} x {numero} = {resultado}")

def exercicio_6():
    try:
        lista_numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        soma = 0

        for x in lista_numeros:
            soma += x
        print(f"A soma é de {soma}")

    except:
        print("Ocorreu um erro!")

def exercicio_7():
    try:
        lista_numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        
        soma = sum(lista_numeros)

        media = soma / len(lista_numeros)
        print(f"A média é de {media}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    exercicio_1()
    print()
    exercicio_2()
    print()
    exercicio_3()
    print()
    exercicio_4()
    print()
    exercicio_5()
    print()
    exercicio_6()
    print()
    exercicio_7()