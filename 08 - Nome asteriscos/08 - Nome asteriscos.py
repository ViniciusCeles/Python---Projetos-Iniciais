# Exercicio: deixar as letras do nome Luiz Otavio entre asteriscos

"""
 012345678910
 Luiz Otavio
"""
nome = 'haytham kenway'
indice = 0 
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome + '*')