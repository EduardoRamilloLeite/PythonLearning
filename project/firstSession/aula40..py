while True:
    num1 = input('Digite um numero:')
    num2 = input('Digite outro numero:')
    operador = input('Digite o operador(+-/*). ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Os numeros digitados sao invalidos')
        continue
        
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido. ')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    if operador == '+':
        print (f'{num1} + {num2}=', num1 + num2)
    elif operador == '-':
        print (f'{num1} - {num2}=',num1 - num2)
    elif operador == '/':
        print (f'{num1} / {num2}=',num1 / num2)
    elif operador == '*':
        print (f'{num1} * {num2}=',num1 + num2)
    else:
        print('nao deveria ter chegado ate aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')    #lower:converte tudo que for maiusculo para minusculo
    print(sair)

    if sair is True:
        break
