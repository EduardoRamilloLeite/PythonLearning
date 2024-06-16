class Teste():
    def __init__ (self, valor):
        self.x = valor   #receber um valor do ususario
    
    """ metodo getter para retornar o valor do atributo x"""
    def get_valor(self):
        return self.x
    
    """metodo setter para atribuir um novo valor ao atributo x"""
    def set_valor(self, v):
        self.x = v


teste = Teste(10)
print('Valor do objeto:', teste.get_valor())

val = int(input('Digite um valor numerico:'))
teste.set_valor(val) #inserir a variavel val dentro da classe

print('Valor do objeto apos atribuicao:', teste.get_valor())
