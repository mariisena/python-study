import math

a = int(input('Valor do cateto adjacente: '))
b = int(input('Valor do cateto oposto: '))
hipotenusa = math.sqrt(a**2 + b**2)
print('Valor da hipotenusa: ', hipotenusa)

'''solution:
a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = (a**2 + b**2) ** 0.5

print(c)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)'''