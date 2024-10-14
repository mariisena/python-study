#a) Implemente um programa que leia o ano de nascimento de uma pessoa e calcule sua idade. verifique se ela já tem idade para votar (16 anos ou mais). Mostre a mensagem informando a situação dela.

ano_atual = int(input("Ano atual: "))
ano_nascimento = int(input("Ano de nascimnento: "))
idade = ano_atual - ano_nascimento
print("A idade é de:", idade)
if idade >= 16:
    print("pode votar")
else:
    print("não pode votar")

#b) Implemente um programa que leia o ano de nascimento de uma pessoa e calcula sua idade. Verifique se ela já tem idade para votar (16 anos ou mais) e para conseguir a CNH - Carteira Nacional de Habilitação (18 anos ou mais).

ano_atual = int(input("Ano atual: "))
ano_nascimento = int(input("Ano de nascimnento: "))
idade = ano_atual - ano_nascimento
print("A idade é de:", idade)
if idade >= 18:
    print("pode votar e pode CNH")
elif idade >= 16:
    print("Pode votar, não pode CNH")
else:
    print("não pode votar, não pode CNH")