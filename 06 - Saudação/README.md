# 06 - Saudação

Este trecho de código funciona como uma saudação automática com base no horário informado pelo usuário:

O programa pede que o usuário digite um número inteiro que representa a hora do dia (por exemplo, 9, 14 ou 20).
Em seguida, tenta converter esse número digitado para o tipo inteiro. Se o usuário digitar algo que não é um número, como letras ou símbolos, o programa detecta o erro e exibe uma mensagem dizendo que só aceita números inteiros.

Se a conversão funcionar, ele analisa o número para decidir qual saudação usar:
    Se for de 0 até 11, o programa imprime “Bom dia”.
    Se for de 12 até 17, imprime “Boa tarde”.
    Se for de 18 até 23, imprime “Boa noite”
    Se o número for maior que 23 (por exemplo, 25 ou 100), ele avisa que o valor é maior do que o permitido, já que não existe uma hora 25 no dia.