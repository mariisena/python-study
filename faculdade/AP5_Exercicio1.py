#Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada. A função main chama a função passando os dois argumentos lidos, ou seja, digitados pelo usuário. 

def msg_num(mensagem, numero):
  print(mensagem, numero)
def main():
  mensagem = str(input("Digite a sua mensagem: "))
  numero = int(input("Digite um número: "))
  msg_num(mensagem, numero)
if __name__ == "__main__":
  main()