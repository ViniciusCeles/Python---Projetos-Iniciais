#Primeiro Digito
cpf_enviado = input('cpf: ')
multiplica = 10
soma_digitos = 0

for digito in cpf_enviado:
    if multiplica >= 2: 
        if digito.isdigit():
            soma_digitos += int(digito) * multiplica
            multiplica -= 1

pri_digito = soma_digitos * 10     
pri_digito %= 11 

pri_digito = 0 if pri_digito > 9 else pri_digito

#Segundo Digito
multiplica_2 = 11
soma_digitos_2 = 0

for digito in cpf_enviado:
    if multiplica_2 >= 3: #vai até antes do digito
        if digito.isdigit():
            soma_digitos_2 += int(digito) * multiplica_2
            multiplica_2 -= 1

soma_digitos_2 += pri_digito * 2 #soma com o valor do Primeiro Digito que ja foi calculado la em cima

seg_digito = soma_digitos_2 * 10     
seg_digito %= 11 

seg_digito = 0 if seg_digito > 9 else seg_digito

if cpf_enviado[:9] + str(pri_digito) + str(seg_digito) == cpf_enviado:
    print(f'O CPF: {cpf_enviado} é válido')  
else:
    print('CPF digitado Inválido')
    print(f'O primeiro digito do CPF é {pri_digito}') 
    print(f'O segundo digito do CPF é {seg_digito}')
    print(f'Os que vc digitou foram: {cpf_enviado[9]} e {cpf_enviado[10]}')