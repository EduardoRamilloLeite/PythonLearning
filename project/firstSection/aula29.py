#try/except
numero_str = input ('vou dobra o numero que vc digitar ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} e {numero_float *2:.2f}') 
except:
    print('isso nao e um numero')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobre de {numero_str} e {numero_float *2:.2f}')
# else:
#     print('isso nao e um numero ')