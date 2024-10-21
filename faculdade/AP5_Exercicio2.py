#Implemente uma função que calcula a idade de uma pessoa. Ela recebe o ano de nascimento da pessoa, faz o cálculo e retorna à idade. A função principal (main) lê o ano de nascimento digitado pelo usuário, chama a função e mostra o valor retornado pela função calcula.

def idade_pessoa(ano_atual, ano_nascimento):
  idade = ano_atual - ano_nascimento
  return idade
def main ():
  ano_atual = int(input("Digite ano atual: "))
  ano_nascimento = int(input("Digite ano de nascimento: "))
  idade = idade_pessoa(ano_atual, ano_nascimento)
  print(f"Tem {idade} anos.")

main()
