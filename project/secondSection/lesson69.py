"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z): #Parametros
    # Definição
    print(f'{x=} {y=} z={z}', '|', 'x + y + z = ', x + y + z)


#Argumentos posicional (1 pra X  , 2 pra Y e 3 pra Z)
soma(1, 2, 3)
soma(1, y=2, z=5)   

print(1, 2, 3, sep='-') 