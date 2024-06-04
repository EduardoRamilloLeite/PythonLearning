import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000)) #caso eu prescise salvar algo na memoria do computador é melhor usar o generator

print(sys.getsizeof(lista)) #mostra o tamanho em byte da funcao
print(sys.getsizeof(generator)) 

print(generator)

# for n in generator:
#     print(n)s