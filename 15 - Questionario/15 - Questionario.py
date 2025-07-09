#EXERCICIO - Sistema de perguntas e respostas
# exiba a Pergunta, as Opções enumeradas e faça uma validação de resposta

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '5', '4'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

# Exibe a pergunta
for questão in perguntas:
    print()
    print(questão['Pergunta'])
    
    # Exibe as alternativas enumeradas
    for i, opcao in enumerate(questão['Opções']):
        print(f'{i}) {opcao}')
    print()

    # Solicita uma alternativa
    escolha = input('Escolha uma resposta: ')

    num_opcoes = len(questão['Opções'])
    
    # Verifica se a escolha é um número e se for valida verifica se a resposta esta certa ou não
    if escolha.isdigit() and int(escolha) >= 0 and int(escolha) < num_opcoes:
        if questão['Opções'][int(escolha)] == questão['Resposta']:
            print('Acertou!!')
            qtd_acertos += 1
        else:
            print('Errou')
    if not escolha.isdigit():
        print('digite uma alternativa válida')

    else:
        print('Escolha invalida')

print('Quantidade de acertos:', qtd_acertos)
        