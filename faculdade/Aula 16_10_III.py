# Implemente a função calcula o dobro. Ela recebe um valor, calcula o dobro e retorna o valor calculado. Não use o print dentro desta função. A função principal (main) lê um valor, chama a função passando o argumento (o valor lido) e mostra o valor retornado pela função calcula o dobro.

def calcula_dobro(p_valor):
    dobro = p_valor * 2
    return dobro
def calcula_triplo(p_valor):
    triplo = p_valor * 3
    return triplo
if __name__ == '__main__':
    valor = int(input("Valor: "))
    valor_retorno = calcula_dobro(valor)
    print("Valor retornado pela função: ", valor_retorno)
    valor_retorno2 = calcula_triplo(valor)
    print("Valor retornado pela função (triplo): ", valor_retorno2)