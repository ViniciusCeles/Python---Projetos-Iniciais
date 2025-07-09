#Exercícios com funções

#Crie uma função que multiplica todos os argumentos não nomeados recebidos
#Retorne o total para uma variavel e mostre o valor dela

#Crie uma função que fala se o numero é impar ou par
#retorne se o numero é par
 
def multiplica(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def par_ou_impar(valor):
    é_par = 'par' if valor % 2 == 0 else 'impar'
    return é_par


total = multiplica(5,5,10)
par_impar = par_ou_impar(total)
print(f'O valor do produto é: {total} e esse número é {par_impar}')
