"""
Faça uma lista de compras
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista enumerados
Não permita que o programa quebre com erros de índices inexistentes
"""
import os

lista = []


while True:
    print('Selecione uma opção')
    pergunta = input('[i]nserir [a]pagar [l]istar: ')
    
    # opção inserir
    if pergunta == 'i':
        inserir = input('Digite oq deseja inserir: ')
        lista.append(inserir)
        os.system('cls')
    
    # opção apagar
    elif pergunta == 'a':
        try:
            apagar = int(input('Digite o numero do item que deseja apagar: '))
            lista.pop(apagar)
        except: # aqui é recomendado tratar os erros diferentes que podem surgir (IndexError ou TypeError) e fazer um except para cada erro (except IndexError: / exceptTypeError: )
            print('Desculpe, não foi possível apagar este item')
    
    # opção listar
    elif pergunta == 'l': 
        os.system('cls')
        if lista == []: # verifica se a lista esta vazia
            print('Não há itens registrados')
        for n, item in enumerate(lista):
            print(n, item)
        