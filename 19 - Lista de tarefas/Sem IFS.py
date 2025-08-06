# EXECUTANDO SEM OS IF, ELIF E ELSE
# Criei um dicionario ""comandos" que possui o nome das funções como chave
    # cada chave tem o valor que corresponde a uma função lambda que retorna a função correspondente a chave
    # a variavel entrada é usada na variavel executar
    # executar é igual a comandos[entrada] onde vai executar lambda se a chave existir, se não ele executa adicionar
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

def importar(tarefas):
    try:
        with open("aula119-lista2.json", "r", encoding="utf8") as lista: #ler arquivo "aula119-lista.json"
            dados = json.load(lista) #dados = informações do arquivo "aula119-lista.json"
            return dados #retornar dados
    except:
        print("Criando arquivo") 
        salvar(tarefas) #se não existir, então ele cria arquivo
    return []

def salvar(tarefas):
    with open("aula119-lista2.json", "w", encoding="utf8") as lista: #escrever arquivo "aula119-lista.json"
        json.dump(tarefas, lista, indent= 2) #despeja tarefas no arquivo "aula119-lista.json"

lista_tarefas = importar([]) #return dados
item_adicionado = []
    

while True:
    print("\nComandos: listar, desfazer, refazer")
    entrada = input("Digite uma tarefa ou comando: ")
    if entrada == "sair":
        break
    comandos = {
        "listar" : lambda: listar(lista_tarefas), 
        "desfazer": lambda: desfazer(lista_tarefas, item_adicionado), 
        "refazer": lambda: refazer(lista_tarefas, item_adicionado),
        "clear": lambda: os.system('cls'), 
        "adicionar" : lambda: adicionar(lista_tarefas, entrada),
    }

    executar = comandos.get(entrada) if comandos.get(entrada) is not None else comandos['adicionar']
    executar()
    salvar(lista_tarefas)