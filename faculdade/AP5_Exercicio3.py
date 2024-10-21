#A função main lê os dois valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.

def valores_inteiros(numero1, numero2):
  resultado = '''??''' #não especificada a operação
  return resultado
def main():
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))

  resultado = valores_inteiros(num1, num2)
  print("O resultado é de: ", resultado)

main()
