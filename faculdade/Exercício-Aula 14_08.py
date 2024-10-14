# A água é um nuriente essencial. Sem ela, o corpo não pode funcionar com perfeição. Cada pessoa precisa de uma quantidade diferente de água para hidratat o corpo. A dose ideal, ou seja, a necessidade diária em litros é calculas através da fórmula> massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.

valor_peso = float(input("Digite o seu peso: "))
agua_diaria = valor_peso*0.03
print(f"Água diária: {agua_diaria:.3f}")