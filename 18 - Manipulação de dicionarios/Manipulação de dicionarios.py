# copy, sorted, produtos.sort

import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a cima em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
    {**item, 'preco': round(item['preco'] * 1.1, 2)}
        for item in novos_produtos
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key= lambda i: i['nome'], reverse= True)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preço = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preço = sorted(produtos_ordenados_por_preço, key= lambda i: i['preco'])

print('Produtos: ')
for i in produtos:
    print(i)
print()
print('Preço 10%: ')
for i in novos_produtos:
    print(i)
print()
print('Por nome: ')
for i in produtos_ordenados_por_nome:
    print(i)
print()
print('Por preço: ')
for i in produtos_ordenados_por_preço:
    print(i)