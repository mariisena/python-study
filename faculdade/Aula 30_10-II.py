def soma(a, b):
    soma = a + b
    return soma


def subtrai(a, b):
    subtrai = a - b
    return subtrai


def main():
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    escolha = str(input("Escolha o número:\n[+] somar\n[-] subtrair\n"))
    if escolha == '+':
        resultado_soma = soma(a, b)
        print(f"{a} + {b} = {resultado_soma}")
    elif escolha == '-':
        resultado_subtrai = subtrai(a, b)
        print(f"{a} - {b} = {resultado_subtrai}")
    else:
        print("Opção inválida")

main()