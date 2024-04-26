"""
desempacotamento + tuples (tuplas)
tupla, imutavel daa pra usar sempre que quiser uma lista que nao prescise mudar o valor 
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)


#tuple
nomes = ['Maria', 'Helena', 'Luiz'] #lista normal
nomes = tuple(nome)                 #transformando lista em tuple
