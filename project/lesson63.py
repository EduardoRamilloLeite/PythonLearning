"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'  #variavel é igual a 'valor' se a condiçao for verdadeira, senao 'outro valor'

# print(variavel)
digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0 #digito vai ser o mesmo valor de digito se o o digito for maior que 9
novo_digito = 0 if digito > 9 else digito

# print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')