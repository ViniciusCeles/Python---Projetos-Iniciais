# 12 - Calculo CPF

Este script em Python tem como objetivo verificar se um número de CPF informado pelo usuário é válido, com base nos algoritmos oficiais de cálculo dos dígitos verificadores.

Entrada do CPF: O usuário insere um CPF completo com 11 dígitos.

Cálculo do 1º dígito verificador: 
    Multiplica os 9 primeiros dígitos por uma sequência decrescente de 10 a 2.
    Soma os resultados,multiplica o total por 10 e em seguida, calcula-se o resto da divisão da soma por 11
    Se o resto for maior que 9 então o digito é 0
    Se o resto for menor que 9 então o digito é o próprio resto

Cálculo do 2º dígito verificador: 
    Usa os 9 primeiros dígitos + o 1º dígito já calculado.
    Multiplica por uma sequência decrescente de 11 a 2.
    Soma os resultados, multiplica o total por 10 e em seguida, calcula-se o resto da divisão da soma por 11
    Se o resto for maior que 9 então o digito é 0
    Se o resto for menor que 9 então o digito é o próprio resto

Validação:
    Compara os dois dígitos calculados com os dígitos fornecidos.
    Informa se o CPF é válido ou não e exibe os valores calculados.

Observações:
Este código considera que o usuário digitará exatamente 11 caracteres, podendo incluir ou não pontuação.
Apenas os dígitos são considerados nos cálculos.
Não há verificação de CPFs com padrões inválidos (ex: todos os dígitos iguais).