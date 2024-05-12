"""
Exercício Distancia 1016
"""

X = int(input())

print(f"{2 * X} minutos")

##########################################################################################

"""
Exercício Fatorial simples 1153
"""

N = int(input())

fat = 1

for i in range(1, N+1):
    fat *= i

print(fat)

#############################################################################################

"""
Eercício Ida a Feira 1281
"""

N = int(input())

for i in range(N):
    M = int(input())

    valores = {}

    for i in range(M):
        fruta, valor = input().strip().split(' ')

        valores[fruta] = float(valor)


    P = int(input())

    resposta = 0.0
    for i in range(P):
        fruta, quantidade = input().strip().split(' ')

        resposta += int(quantidade) * valores[fruta]


    print(f'R$ {resposta:.2f}')

#############################################################################################


"""
Exercício Identificando o Chá 2006
"""

def contar_respostas_corretas(cha_real, respostas):
    return respostas.count(cha_real)


cha_real = int(input())


respostas = list(map(int, input().split()))

numero_corretas = contar_respostas_corretas(cha_real, respostas)


print(numero_corretas)


##############################################################################################

"""
Exercício Aviões de Papel 2339
"""

C, P, F = [int(x) for x in input().strip().split(' ')]

if P >= C * F:
    print('S')

else: 
    print ('N')

###################################################################################################

"""
Exercício Tacógrafo 2388
"""

def calcular_distancia(tempo, velocidade):
    return tempo * velocidade

N = int(input())

distancia_total = 0

for i in range(N):
   
    tempo, velocidade = map(int, input().split())
   
    distancia_total += calcular_distancia(tempo, velocidade)

print(distancia_total)

######################################################################################################
"""
Exercício Busca na Internet 2413
"""

t = int(input())

print(4 * t)

#######################################################################################################
"""
Exercício Sequência Secreta 3048
"""


N = int(input())

sequencia = [int(input()) for _ in range(N)]

num_marcados = 1

for i in range(1, N):

    if sequencia[i] != sequencia[i - 1]:
        num_marcados += 1
    

print(num_marcados)











