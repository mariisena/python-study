def soma(num1, num2):
    resultado = num1 + num2
    return resultado


def soma_2(num1, num2):
    return num1 + num2


def main():
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    resultado = soma(num1, num2)
    print(f"A soma de {num1} + {num2} é igual a: {resultado}")

    resultado2 = soma(2.1, 3.3)
    print(f"A soma de 2.1 + 3.3 é igual a: {resultado2}")
  
    print("A soma é de:", soma_2(num1, num2))

main()