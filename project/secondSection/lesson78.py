# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplica(duplicar):
     return duplicar * 2

def triplica(triplica):
     return triplica * 3

def quadruplica(quadruplica):
     return quadruplica * 4

numero = int(input('Digite um numero:'))

print (duplica(numero))
print (triplica(numero))
print (quadruplica(numero))

#Resposta intelligente

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))