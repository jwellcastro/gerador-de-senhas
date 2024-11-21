import random
import string

def gerar_senha(tipo, tamanho=12):
    if tipo == 'numérica':
        caracteres = list(string.digits)
    elif tipo == 'alfanumérica':
        caracteres = list(string.ascii_letters + string.digits)
    else:
        caracteres = list(string.ascii_letters + string.digits + string.punctuation)
    senha = []
    for _ in range(tamanho):
        senha.append(random.choice(caracteres))
    
    random.shuffle(senha) #embaralha a lista para uma distribuição mais aleatória
    return ''.join(senha) #transforma a lista em string

if __name__ == '__main__':
    print('Defina o tipo de senha: ')
    print('1 - Numérica')
    print('2 - Alfanumérica')
    print('3 - Alfanumérica com caracteres especiais')

    opcao = int(input('Digite a opção desejada: ')) 
    if opcao == 1:
        tipo = 'numérica'

    elif opcao == 2:
        tipo = 'alfanumérica'
    
    else:
        tipo = 'alfanumérica com caracteres especiais'
    
    tamanho = int(input('Digite o tamanho da senha que você deseja: '))

    senha_gerada = gerar_senha(tipo, tamanho)
    print('Senha gerada: ', senha_gerada)