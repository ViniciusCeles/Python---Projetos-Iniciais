"""
Faça um jogo para o usuário adivinhar qual a palavra secreta
Proponha um palavra e de a possibilidade de digitar uma letra
A letra deve ser checada se está na palavra secreta
    Se ela estiver: exiba a letra
    Se não: exiba um *
Faça a ontagem de tentativas
"""
import os #usado para importar o os.system('clear')

palavra_secreta = 'escritorio'
letras_acertadas = ''
tentativas = 0 

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if letra_digitada == 'sair':
        break
 
    #verifica se a entrada tem mais de uma letra, se é numero ou se não é uma letra
    if len(letra_digitada) > 1 and letra_digitada != palavra_secreta:
        print('Digite apenas uma letra')
        continue
    elif letra_digitada.isdigit():
        float(letra_digitada)
        print('Numeros não são validos, digite apenas letras')
        continue
    elif not letra_digitada.isalnum():
        print('Digite apenas letras')
        continue

    if letra_digitada in palavra_secreta: #verifica se a entrada esta na palavra secreta
        letras_acertadas += letra_digitada
    
    palavra_resultado = ''          
    for letra in palavra_secreta: #para cada letra da palavra secreta, 
        if letra in letras_acertadas: #verifica se a letra esta nas letras acertadas 
            palavra_resultado += letra #em seguida adiciona a letra na palavra resultado,
        else:
            palavra_resultado += '*' #caso contrario adiciona um asterisco

    print(palavra_resultado)
    
    if palavra_resultado == palavra_secreta:
        os.system('cls') #limpa o terminal 
        print(f'VOCE GANHOU !! A palavra secreta era "{palavra_secreta}"')
        print(f'Numero de tentativas: {tentativas}')
        letras_acertadas = ''
        tentativas = 0
        palavra_resultado = ''
        print()
        sair = input('deseja sair? ')
        if sair.endswith('m'):
            print('vc saiu do jogo')
            break
        else:
            continue