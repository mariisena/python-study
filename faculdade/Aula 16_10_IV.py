# Crie uma função para somar dois valores. Ela recebe os dois valores, calcula a soma e retorna o resultado do cálculo.
#A função main lê os dois valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.

def somar_valores(a, b):
  soma = a + b
  return soma
def main():
  num_1 = int(input("Primeiro número: "))
  num_2 = int(input('Segundo número: '))
  soma_dos_numeros = somar_valores(num_1, num_2)
  print("A soma é de: ", soma_dos_numeros)

if __name__ == "__main__":
  main()