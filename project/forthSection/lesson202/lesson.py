# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

#expande a home do usuario (expand user)
HOME = os.path.expanduser('~') 

#unindo a home com o desktop
DESKTOP = os.path.join(HOME, 'Desktop')
 
#vai copiar tudo que tem dentro dessa pasta pra outra que vai criar
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')

NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

#criando nova pasta
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file) #caminho original do arquivo
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)