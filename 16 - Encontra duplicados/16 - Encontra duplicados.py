"""
Exercício
Crie uma função que encontra o primeiro e segundo numero duplicado das listas
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_duplicados(lista_atual):
    duplicado1 = -1
    duplicado2 = -1
    checados = set()
    contagem_duplicados = 0
    for numero in lista_atual:
        if numero in checados and contagem_duplicados <1:
            duplicado1 = numero
            contagem_duplicados += 1
        if numero in checados and numero != duplicado1 and contagem_duplicados >0:
            duplicado2 = numero
            return duplicado1, duplicado2
        checados.add(numero) 
    return duplicado1, duplicado2
    
for lista in lista_de_listas_de_inteiros:
    print('\n',lista, encontrar_duplicados(lista))
