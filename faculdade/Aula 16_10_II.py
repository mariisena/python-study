# Crie uma função (def) que recebe um valor e mostra o valor recebido. A função main (principal) chama a função três vezes, passa um valor inteiro, um valor float e depois um valor negativo.

def mostra_valor(p_valor):
    print("Parâmetro recebido: ", p_valor)
if __name__ == '__main__':
    print("Iniciando programa...")

    mostra_valor(5)
    mostra_valor(23.8)
    mostra_valor(-55)

    print("Programa finalizado")