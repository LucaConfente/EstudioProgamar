"""
AC3
Exercício 1: triângulos
Desenvolva uma função determina_tipo_triangulo que recebe três lados de um triângulo e retorna uma string,
 "Escaleno", "Isósceles" ou "Equilátero", 
conforme o tipo do triângulo. A função deve retornar 
"Não é um triângulo" se os três lados não formarem um triângulo. Use a função abaixo como 
teste:

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
"""

def determina_tipo_triangulo(l1, l2, l3):
    if (l1 <= 0) or (l2 <= 0) or (l3 <= 0) and (l1 + l2 > l3) or (l2 + l3 > l1) or (l1 + l3 > l2) :
         return ("triângulo não existe")
    if (l1 == l2 == l3):
        return("Equilátero")
    elif ((l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 != l1)) :
        return("Isósceles")
    elif (l1 != l2 != l3) and (l2 != l1 != l3):
        return("Escaleno")
    
    else:
        return("Não é um triângulo")
print(determina_tipo_triangulo(10, 4, 4))


"""
if ((l1 + l2 <= l3) or (l3 + l1 <= l2) or (l2 + l3 <= l1)):
        return("Não é um triângulo")
"""
"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que recebe um número inteiro e retorna uma string
indicando o dia da semana equivalente, considerando que o dia da semana igual a 1 é o domingo,
2 é segunda-feira, etc. A função deve retornar uma string vazia caso o número seja inválido.
 Use a função abaixo como teste:

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia
"""

def dia_semana(dds):
    if dds == 1:
        return("Domingo")
    elif dds == 2:
        return("Segunda-feira")
    elif dds == 3:
        return("Terça-feira")
    elif dds == 4:
        return("Quarta-feira")
    elif dds == 5:
        return("Quinta-feira")
    elif dds == 6:
        return("Sexta-feira")
    elif dds == 7:
        return("Sábado")
    else:
        return("string vazia")

print(dia_semana(8))

"""
Exercício 3: calculadora simples
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao, 
que recebem dois números cada uma e retornam o resultado da operação indicada. 
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), 
que lê dois números e uma operação e exibe na tela o valor do resultado, ou exibe "operação inválida" 
se o usuário inserir uma mensagem diferente das quatro operações.

Exemplos
Informe um número: 5.5
Informe outro número: 10
Informe a operação: soma
Resultado: 15.5
Informe um número: 5.5
Informe outro número: 10
Informe a operação: multiplicação
Resultado: 55.0
Informe um número: 5.5
Informe outro número: 10
Informe a operação: abcd
operação inválida

"""



def calculadora(a, oper, b):
    
    if oper == "soma":
        print("O Resultado é", (a + b)) 

    elif oper == "subtração":
            print("O Resultado é", (a - b))

    elif oper == "multiplicação":
            print("O Resultado é", (a * b))

    elif oper == "divisão":
            print("O Resultado é", (a / b))

    else:
        print("operação inválida")

calculadora(9, "subtração", 9)
        


"""
def calculadora():
   
    a = print(input("Informe um numero:"))
    b = print(input("Informe um numero:"))
    oper = print(input("Informe a oper:"))

    if oper == "soma":
        print("O resultado é:",(a + b) )

    if oper == "subtração":
        print("O resultado é:",(a - b) )

    if oper == "multiplicação":
        print("O resultado é:",(a * b) )

    if oper == "divisão":
        print("O resultado é:",(a / b) )

    else:
        print("operação inválida")

calculadora()
"""