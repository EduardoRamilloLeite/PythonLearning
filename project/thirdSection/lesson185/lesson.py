# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

#DATACLASSES
# Em Python, dataclasses é um módulo introduzido na versão 3.7, que fornece uma maneira simples de criar
# classes usadas principalmente para armazenar dados. As dataclasses automatizam a criação de métodos básicos, 
# como o inicializador (__init__), o representador (__repr__), e outros métodos úteis, como a comparação (__eq__), entre outros. 
# Isso facilita muito a vida do programador, que não precisa escrever manualmente esses métodos repetitivos para classes que são
# principalmente "containers" de dados.

#REPR
# O método __repr__ em Python é um método especial usado para definir a representação "oficial" de uma instância de classe.
# Ele deve retornar uma string que idealmente deve ser uma expressão Python válida que poderia ser usada para recriar o objeto
# com o mesmo estado. Isso é útil para depuração e log, pois fornece uma representação clara e detalhada do objeto.



from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(p1.nome_completo)