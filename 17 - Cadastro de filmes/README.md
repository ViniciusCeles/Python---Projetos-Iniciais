# 17 - Cadastro de filmes

Este é um sistema de cadastro e consulta de filmes, feito em Python. Ele funciona como um pequeno programa interativo, que permite ao usuário realizar quatro ações principais: adicionar, visualizar todos os filmes cadastrados, buscar filmes por gênero ou encerrar o programa.

Ao iniciar, o programa exibe uma mensagem de boas-vindas e apresenta um menu com as quatro opções enumeradas:

Cadastrar novo filme: Se o usuário escolher essa opção, o sistema pergunta pelo título do filme, o ano em que foi lançado e o gênero. Esses dados são armazenados juntos, como se fossem uma ficha de cadastro. O filme é então guardado em uma lista de filmes.

Listar todos os filmes: Aqui, o programa mostra todos os filmes que já foram cadastrados, um por um, com seus respectivos títulos, anos e gêneros.

Buscar filmes por gênero: O programa coleta todos os gêneros disponíveis entre os filmes cadastrados e os mostra como opções. O usuário escolhe um deles e o sistema lista apenas os filmes que pertencem ao gênero selecionado.

Sair: Finaliza o programa.

Antes de qualquer ação, o programa verifica se a opção escolhida é válida. Se o usuário digitar algo errado, como uma letra ou um número fora das opções, ele avisa e volta a mostrar o menu. Durante o cadastro de um filme, também verifica se o ano informado contém apenas números.