"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input('Digite um número inteiro: ')

try:
    numero_digitado_int = int(numero_digitado)    
    if numero_digitado_int % 2 == 0:
        print(f'{numero_digitado_int} é par')
    else:
        print(f'{numero_digitado_int} é impar')
except:
    print('Voce não digitou um numero inteiro')
