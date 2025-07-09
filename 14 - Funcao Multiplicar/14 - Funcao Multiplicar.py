#EXERCICIO
#Crie funcoes que duplicam, triplicam e quadruplicam o numero recebido

def criar_multiplicador(multiplicador):
    def calcular(numero):
        return numero * multiplicador
    return calcular #apenas retorna mas não executa


duplicar = criar_multiplicador(2) #retorna calcular com o multiplicador 2
triplicar = criar_multiplicador(3) #retorna calcular com o multiplicador 3
quadruplicar = criar_multiplicador(4) #retorna calcular com o multiplicador 4

print(duplicar(2)) #EXECUTA calcular com o multiplicador 2 e numero 2
print(triplicar(2)) #EXECUTA calcular com o multiplicador 3 e numero 2
print(quadruplicar(2)) #EXECUTA calcular com o multiplicador 4 e numero 2

