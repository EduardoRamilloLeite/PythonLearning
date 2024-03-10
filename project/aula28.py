nome = input('Digite seu Nome: ') 
idade = input('Digite sua idade: ') 
letras  = len(nome[::])
primeiraLetra = (nome[0:1])
ultimaLetra = (nome[:-2:-1])

if not nome and not idade:
    print('desculpe vc deixou os campos vazio')

else:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')
    # o nome contem espacos
    print(f'seu nome contem {letras} letras' )
    print(f'A primeira letra do seu nome e: {primeiraLetra}')
    print(f'A ultima letra do seu nome e: {ultimaLetra}')  


# Resposta do professor
    
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade: #1---------
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome: #2--------
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')#3--------
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")