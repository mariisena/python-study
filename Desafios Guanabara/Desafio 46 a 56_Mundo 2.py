def desafio46():
    from time import sleep
    for x in range(10, -1, -1):
        print(x)
        sleep(0.5)
    print("FOGO!")

def desafio47():
    for x in range(0, 51, 2):
        print(x)
    print('FIM')

def desafio48():
    ct = 0
    s = 0
    for x in range(0,501,3):
        if x % 2 != 0:
            print(x)
            s += x
            ct += 1
    print(f"A soma de todos os {ct} valores é de {s}")

def desafio49():
    num = int(input("Digite um número para ver sua tabuada: "))
    for x in range(1, 11):
        resultado = num * x
        print(f"{num} x {x} = {resultado}")
        
def desafio50():
    soma = 0
    for i in range(6):
        num = int(input("Digite um número: "))
        if num % 2 == 0:
            soma += num
    print(f"A soma dos números pares é: {soma}")

def desafio51():
    primeiro = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    decimo = primeiro + (10 - 1) * razao
    for i in range(primeiro, decimo + razao, razao):
        print(i, end=' → ')
    print("fim")


#run
desafio51()