'''Digite a seguinte expressão no interpretador:
10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
Tente resolver o mesmo cálculo a mão, usando apenas lápis e papel. Observe como a prioridade das operações é importante'''

print(10 % 3 * 10**2 + 1 - 10 * 4 / 2)


'''gabarito livro'''
# Arquivo: capitulo 02/exercicio-02-02.py
##############################################################################
# O resultado da expressão:
# 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# é 81.0
#
# Realizando o cálculo com as prioridades da página 39,
# efetuando apenas uma operação por linha,
# temos a seguinte ordem de cálculo:
# 0 --> 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# 1 --> 10 % 3 * 100     + 1 - 10 * 4 / 2
# 2 --> 1      * 100     + 1 - 10 * 4 / 2
# 3 -->          100     + 1 - 10 * 4 / 2
# 4 -->          100     + 1 - 40     / 2
# 5 -->          100     + 1 - 20
# 6 -->          101         - 20
# 7 -->                        81