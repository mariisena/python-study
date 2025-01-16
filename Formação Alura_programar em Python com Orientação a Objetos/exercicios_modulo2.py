#Exercicio 1
def exercicio_1():
    numero = int(input("Insira um número: "))
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

def exercicio_2():
    idade = int(input("Digite a sua idade: "))
    if 0 >= idade <= 12:
        print("CRIANÇA")
    elif 13 >= idade <= 18:
        print("ADOLESCENTE")
    else:
        print("ADULTO")

def exercicio_3():
    usuario_correto = 'Valentina'
    senha_correta = 123456

    usuario = str(input("Digite seu nome: "))
    senha = int(input("Digite uma senha: "))

    if usuario_correto == usuario and senha_correta == senha:
        print("Login bem sucedido!")
    else:
        print("Credenciais inválidas. Tente novamente.")

def exercicio_4():
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante")
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante")
    else:
        print("O ponto está sobre um eixo ou na origem.")

def main():
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()

if __name__ == '__main__':
    main()