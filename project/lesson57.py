import os

lista_de_compras = []

while True:
    opcao = input('Selecione uma opçao:  [i]nserir [a]pagar [l]istar: ')
    if opcao == 'i':
        items = input('Valor: ')
        lista_de_compras.append(items)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('clear')

        if len(lista_de_compras) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')