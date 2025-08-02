# O programa deve exibir um menu com as opções:
# 1. Cadastrar novo filme
# 2. Listar todos os filmes
# 3. Buscar filmes por gênero
# 4. Sair

# Cada filme deve ser armazenado como um dicionário com as seguintes informações:
# título
# ano
# gênero
# Os filmes devem ser armazenados em uma lista.

# Ao escolher a opção 3, o usuário digita um gênero e o programa mostra todos os filmes daquele gênero.

# Dica:
# Use um loop while para manter o menu funcionando até que o usuário escolha sair. Use input() para coletar

# Extras (se quiser ir além):
# Validar se o ano é um número.
# Permitir cadastrar mais de um gênero por filme.
# Salvar os dados em um arquivo .txt (nível intermediário).

opcoes = ['Cadastrar novo filme', 'Listar todos os filmes', 'Buscar filmes por gênero', 'Sair']
filmes = []
generos = set()


while True:
    print('\nOlá, esse é o sistema de cadastro de filmes') #Introdução
    for i, opcao in enumerate(opcoes, 1): #Mostra opcoes
        print(f'{i}) {opcao}')
    
    escolha = input('Escolha uma das opções: ') #Pede entrada de uma das opcoes
    print()
    
    try: #Valida a escolha
        escolha = int(escolha) 
        if escolha > len(opcoes) or escolha < 1:
            print(f'\nEscolha uma opção de 1 a {len(opcoes)}\n')

    except ValueError:
        print(f'\nUma opção de 1 a {len(opcoes)}. Letras não são uma opção válida\n')

    if escolha == 1: #Cadatrar filme
      titulo = input('Digite o titulo do filme: ')  
      ano = input('Digite o ano do filme: ')
      
      if not ano.isdigit():
          print('Digite apenas numeros para o ano')
          continue
      
      genero = input('Digite o genero do filme: ')
      filme_novo = {'titulo' : titulo, 'ano' : ano, 'genero' : genero}
      filmes.append(filme_novo)

    elif escolha == 2: #Mostrar filmes cadastrados
        for filme in filmes:
            print(f'Titulo: {filme['titulo']}')
            print(f'Ano: {filme['ano']}')
            print(f'Genero: {filme['genero']}')
            print()

    elif escolha == 3: #Filtrar filmes
        print('Escolha um dos generos:')
        generos = sorted(set(filme['genero'] for filme in filmes))
        for i, genero in enumerate(generos,1):
            print(f'{i}) {genero}')
        try:
            genero_escolhido = int(input('escolha um genero: '))
            genero_escolhido -= 1
            genero_escolhido = generos[genero_escolhido]

        except (ValueError, IndexError):
            print('Genero inválido')
            continue

        print(f'\nFilmes do genero {genero_escolhido}:')
        for filme in filmes:
            if filme['genero'] == genero_escolhido:
                print(f" - {filme['titulo']} ({filme['ano']})")

    elif escolha == 4: #Sair
        print('Saindo...')
        break

#olha meu comentario aqui