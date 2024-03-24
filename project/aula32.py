#exercicio
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numeroDigitado = int(input('Digite um numero inteiro: '))

if numeroDigitado % 2 == 0:
             print('Esse número é par!')
else:
            print('Ele é ímpar!')   



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora: ')

try:
    horas = int(entrada) #convertendo pra num inteiro

    if horas >= 0 and horas <= 11:
        print('Bom dia')
    elif horas >= 12 and horas <= 17:
        print('Boa tarde')
    elif horas >= 18 and horas <=23:
        print('Boa noite' )
    else:
        print('Nao conheco essa hora')

except:
    print('Digite um numero inteiro')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('digite seu primeiro nome: ')
tamanhoNome = len(nome)

if tamanhoNome > 1:
    if tamanhoNome <= 4:
        print('Seu nome é curto')
    elif tamanhoNome >= 5 and tamanhoNome <= 6:
        print('Seu nome é normal')
    else:
        print('seu nome é muito grande')
else:
    print('Digite mais de uma letra: ')
    


