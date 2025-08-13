# O programa deve exibir um menu com as opções:
# 1. Cadastrar novo filme
# 2. Listar todos os filmes
# 3. Buscar filmes por gênero
# 4. Alterar filme
# 5. Excluir filme
# 6. Sair

# Cada filme deve ser armazenado como um dicionário com as seguintes informações:
# título
# ano
# gênero
# Os filmes devem ser armazenados em uma lista.


import json

def importar_lista():
    importados = []
    try:
        with open("lista_filmes.json", "r", encoding="utf8") as lista_filmes:
            importados = json.load(lista_filmes)
        return importados
    except:
        print("criando arquivo...")
        salvar_lista(importados)
        return importados

def salvar_lista(lista):
    with open("lista_filmes.json", 'w', encoding="utf8") as lista_filmes:
        json.dump(lista, lista_filmes, indent=2)

def cadastrar(lista):
    while True:
        titulo = input('Digite o titulo do filme: ')  
        ano = input('Digite o ano do filme: ')
      
        if not ano.isdigit():
            print('Digite apenas numeros para o ano')
            continue
        genero = input('Digite o genero do filme: ')
        filme_novo = {'titulo' : titulo, 'ano' : ano, 'genero' : genero}
        lista.append(filme_novo)
        return filme_novo

def exibir_filmes(lista):
    for filme in lista:
        print(f'Titulo: {filme['titulo']}')
        print(f'Ano: {filme['ano']}')
        print(f'Genero: {filme['genero']}\n')

def filtrar_filmes(lista):
    while True:
        print('Escolha um dos generos:')
        generos = sorted(set(filme['genero'] for filme in lista))
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
        for filme in lista:
            if filme['genero'] == genero_escolhido:
                print(f" - {filme['titulo']} ({filme['ano']})")
        break

def alterar_filmes(lista):
    while True:
        print('Filmes cadastrados:')
        for i, filme in enumerate(lista, 1):
            print(f'{i}) Titulo: {filme['titulo']}')
            print(f'  Ano: {filme['ano']}')
            print(f'  Genero: {filme['genero']}')
            print()
        try:
            alterar = int(input('Escolha um dos filmes: '))
            if alterar < 1 or alterar > len(lista):
                print(f'Digite um numero valido de 1 a {len(lista)}')
                continue
            alterar -= 1
            print(f'1) Titulo: {lista[alterar]['titulo']}')
            print(f'2) Ano: {lista[alterar]['ano']}')
            print(f'3) Genero: {lista[alterar]['genero']}')
            alterar_atributo = int(input('Escolha o que deseja alterar: '))
                
            if alterar_atributo == 1:
                alt_titulo = input('Digite o titulo: ')
                lista[alterar]['titulo'] = alt_titulo
            if alterar_atributo == 2:
                alt_ano = input('Digite o ano: ')
                if not alt_ano.isdigit():
                    print('Digite apenas numeros para o ano')
                    continue
                lista[alterar]['ano'] = alt_ano
            if alterar_atributo == 3:
                alt_genero = input('Digite o genero: ')
                lista[alterar]['genero'] = alt_genero
            else:
                print('Escolha uma opção válida')
            break

        except ValueError:
                print('Digite apenas numeros para selecionar uma das opções')

def excluir_filme(lista):
    while True:
        print('Filmes cadastrados:')
        for i, filme in enumerate(lista, 1):
            print(f'{i}) Titulo: {filme['titulo']}')
            print(f'  Ano: {filme['ano']}')
            print(f'  Genero: {filme['genero']}')
            print()
        try:
            excluir = int(input('Digite qual filme deseja excluir: '))
            if excluir < 1 or excluir > len(lista):
                print(f'Digite numeros validos de 1 a {len(lista)}')
                continue
            excluir -= 1
            lista.pop(excluir)
            print('filme excluido')
            break
        except ValueError:
            print('Digite apenas numeros')

def executar():
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
            print(f'Uma opção de 1 a {len(opcoes)}. Letras não são uma opção válida\n')

        if escolha == 1: #Cadatrar filme
            cadastrar(filmes)

        elif escolha == 2: #Mostrar filmes cadastrados
            exibir_filmes(filmes)

        elif escolha == 3: #Filtrar filmes
            filtrar_filmes(filmes)

        elif escolha == 4: #Alterar filme
            alterar_filmes(filmes)

        elif escolha == 5: #Excluir filme
            excluir_filme(filmes)

        elif escolha == 6: #Sair
            print('Saindo...')
            salvar_lista(filmes)
            break

opcoes = ['Cadastrar novo filme', 'Listar todos os filmes', 'Buscar filmes por gênero','Alterar filme', 'Excluir filme', 'Sair']
filmes = importar_lista()
generos = set()

executar()