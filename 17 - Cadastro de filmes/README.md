# 17 - Cadastro de filmes

Este é um sistema de cadastro e consulta de filmes, feito em Python. Ele funciona como um programa interativo, que permite ao usuário realizar seis ações principais: adicionar, visualizar todos os filmes cadastrados, buscar filmes por gênero, alterar filme, excluir filme ou encerrar o programa.

Ao iniciar, o programa exibe uma mensagem de boas-vindas e apresenta um menu com as seis opções enumeradas:

1) Cadastrar novo filme: Se o usuário escolher essa opção, o sistema pergunta pelo título do filme, o ano em que foi lançado e o gênero. Esses dados são armazenados juntos, como se fossem uma ficha de cadastro. O filme é então guardado em uma lista de filmes.

2) Listar todos os filmes: Aqui, o programa mostra todos os filmes que já foram cadastrados, um por um, com seus respectivos títulos, anos e gêneros.

3) Buscar filmes por gênero: O programa coleta todos os gêneros disponíveis entre os filmes cadastrados e os mostra como opções. O usuário escolhe um de3les e o sistema lista apenas os filmes que pertencem ao gênero selecionado.

4) Alterar filme: Lista filmes e pede para escolher uma das opções e em seguida solicita qual atributo do filme o usuário gostaria de alterar e no final altera o atributo após o usuário digitar o valor

5) Excluir filme: Pergunta qual dos filmes enumerados o usuario gostaria de excluir e no fim exclui se for um valor valido

6) Sair: Salva os filmes cadastrados em um arquivo .json e Finaliza o programa.

Antes de qualquer ação, o programa verifica se a opção escolhida é válida. Se o usuário digitar algo errado, como uma letra ou um número fora das opções, ele avisa e volta a mostrar o menu. Durante o cadastro de um filme, também verifica se o ano informado contém apenas números.