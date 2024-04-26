# nome = 'Luiz Otavio'

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string += '*L*u*i*z* *O*t*a*v*i*o*'


nome = "Luiz Otavio"
nome_com_asteriscos = ""
i = 0
while i < len(nome):
    nome_com_asteriscos += nome[i] + "*"
    i += 1

print(nome_com_asteriscos)
