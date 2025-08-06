import os, json

def listar(lista):
    if len(lista) >0:
        print()
        for i in lista:
            print(i)
    elif len(lista) == 0:
        print("\nLista Vazia")
    return lista

def adicionar(lista, item):
    lista.append(item)
    return item

def desfazer(lista, adicionado):
    if len(lista) <= 0:
        print("Nada a desfazer...")
        return lista
    adicionado.append(lista[-1])
    lista.pop()

def refazer(lista, adicionado):
    if len(adicionado) < 1:
        print('\nNada a refazer')
        return lista
    lista.append(adicionado[-1])
    adicionado.pop()
    return lista

def executando():
    importar(lista_tarefas) #importa dados salvos no arquivo / cria arquivo se não existir
    while True:
        print("\nComandos: listar, desfazer, refazer")
        comando = input("Digite uma tarefa ou comando: ")

        if comando == "listar":
            listar(lista_tarefas)
        elif comando == "desfazer":
            desfazer(lista_tarefas, item_adicionado)
            listar(lista_tarefas)
        elif comando == "refazer":
            refazer(lista_tarefas, item_adicionado)
            listar(lista_tarefas)
        elif comando == "sair":
            salvar(lista_tarefas)
            break
        elif comando == "clear":
            os.system('cls')
        else:
            adicionar(lista_tarefas, comando)
            listar(lista_tarefas)

def importar(tarefas):
    try:
        with open("lista.json", "r", encoding="utf8") as lista: #ler arquivo "lista.json"
            dados = json.load(lista) #dados = informações do arquivo "aula119-lista.json"
            return dados #return dados
    except:
        print("Criando arquivo") 
        salvar(tarefas) #se não existir, então ele cria arquivo
        return []

def salvar(tarefas):
    with open("lista.json", "w", encoding="utf8") as lista: #escrever arquivo "lista.json"
        json.dump(tarefas, lista, indent= 2) #despeja tarefas no arquivo "lista.json"

lista_tarefas = importar([]) #retornar dados
item_adicionado = []

executando()