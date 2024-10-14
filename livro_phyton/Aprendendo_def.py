def soma(a, b):
    print(a+b)
soma(2, 9)
soma(7, 8)
soma(10, 15)


print()

def soma(a, b):
    return a + b
print(soma(2, 9))

print()

def épar(x):
    return x % 2 == 0
print(épar(2))
print(épar(3))
print(épar(10))

print()

def épar(x):
    return x % 2 == 0
def par_ou_impar(x):
    if épar(x):
        return "par"
    else:
        return "impar"
print(par_ou_impar(4))
print(par_ou_impar(5))

print()

#EXERCÍCIO 8.1
def maximo(a, b):
    if a > b:
        return a
    else:
        return b
print(f"maximo(5,6) == 6 -> obtido: {maximo(5,6)}")
print(f"maximo(2,1) == 2 -> obtido: {maximo(2,1)}")
print(f"maximo(7,7) == 7 -> obtido: {maximo(7,7)}")