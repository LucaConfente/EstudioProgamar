
#FEITO NO BEECROWD COM OUTRA CONTA. AS RESPOSTAS VÁLIDAS EU BOTEI AQUI. AINDA NÃO CONSIGO ACESSAR O MEU BEECROWD


"""
Exercício 1161 Soma dis Fatoriais
"""

while True:
    try:
        lista = input().split('')
        M = int(lista[0])
        N = int(lista[0])
        n1=0
        n2=0
        c1 = M - 1
        c2 = N - 1
        if (N >= 0) and (N<=20) and (M >=0) and (M <= 20):
            if n1 == 0:
                n1 = 1
            if n2 == 0:
                n2 = 1
            while c2 > 0:
                n2 += n2 * c2
                c2 -=1
        print(n1+n2)
    except EOFError:
        break
#####################################################################################################
"""
Exercício 1221 Primo Rápido
"""
import math


def Crivo(n):
    C = [True for _ in range(n)]
    primos = []

    C[1] = False
    primos.append(2)

    for i in range(4, n, 2):
        C[i] = False

    for i in range(3, n, 2):
        if(C[i]):
            primos.append(i)

            for j in range(i * 3, n, 2 * i):
                C[j] = False

    return primos


def ehPrimo(primos, n):
    limite = math.ceil(math.sqrt(n))

    for primo in primos:
        if(primo > limite):
            return True
        elif(n % primo == 0):
            return (n == primo)

    return True


primos = Crivo(65536)

N = int(input())

for _ in range(N):
    X = int(input())

    print('Prime' if ehPrimo(primos, X) else 'Not Prime')

#####################################################################################################

"""
Exercício 1171 Frequência de números
"""

n = int(input())

freq = [0 for _ in range(2001)]

for _ in range(n):
    x = int(input())
    
    freq[x] += 1

for i in range(1, 2001):
    if(freq[i] > 0):

        print(f"{i} aparece {freq[i]} vez(es)")

#####################################################################################################

"""
Exercício 1087 Dama
"""
#utilizei o abs para retornar o valor positivo, e o strip pra tirar as possibilidaddes dos espaços em branco no jogo

while True:
    try:
        [X1, Y1, X2, Y2] = [int(x) for x in input().strip().split(' ')]

        if(X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0):
            break

        if(X1 == X2 and Y1 == Y2):
            print('0')

        elif(X1 == X2 or Y1 == Y2 or abs(X1 - X2) == abs(Y1 - Y2)):
            print('1')

        else:
            print('2')

    except EOFError:
        break

#####################################################################################################

"""
Exercício 1028 Figurinhas
"""

def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)


N = int(input())

for _ in range(N):
    Fig1, Fig2 = [int(x) for x in input().strip().split(' ')]
    print(MDC(Fig1, Fig2))

#####################################################################################################

"""
Exercício 1170 Blobs
"""
import math

N = int(input())

for _ in range(N):
    Bl = float(input())

    print(f'{math.ceil(math.log2(Bl))} dias') #arredodamento do numero gerado Bl com o log de base 2

#####################################################################################################

"""
Exercício 1555 Funções
"""

def r(x, y):
    return (3 * x) * (3 * x) + y * y


def b(x, y):
    return 2 * x * x + (5 * y) * (5 * y)


def c(x, y):
    return -100 * x + y * y * y


N = int(input())

for _ in range(N):
    x, y = [int(x) for x in input().strip().split(' ')]

    rafael = r(x, y)
    carlos = c(x, y)
    beto = b(x, y)

    if(carlos > beto and carlos > rafael):
        print('Carlos ganhou')
    elif(beto > carlos):
        print('Beto ganhou')
    else:
        print('Rafael ganhou')

#####################################################################################################

"""
Exercício 1329 Cara ou Coroa
"""

while True:
    try:
        N = int(input())

        ln = [int(x) for x in input().strip().split(' ')]
        maria, joao = 0, 0

        for jogo in ln:
            if(jogo == 0):
                joao += 1
            else:
                maria += 1
        
        print(f"Mary won {maria} times and John won {joao} times")
    except EOFError:
        break