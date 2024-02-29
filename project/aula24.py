#operadores in e not in

nome = 'otavio'

# print (nome[2])
# print (nome[-4])

#print('a' in nome)
#print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}' )
else:
    print(f'{encontrar} nao esta em {nome}')