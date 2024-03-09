#Trabalho AC1

"""
Exercício 1: equações de segundo grau
Elabore um código em Python que resolva uma questão de segundo grau ax² + bx + c = 0. O programa deve ler os
parâmetros a, be cda proposta e deve calcular as raízes pela fórmula de Bhaskara.

"""

#formula bask formula =(float)( a*x**2 + b*x + c)

#Exercício 1

a = 1
b = -6
c = 8

#a = float(input("Digite o valor do coeficiente a:"))
#b = float(input("Digite o valor do coeficiente b:"))
#c = float(input("Digite o valor do coeficiente c:"))

delta = b**2 - 4*a*c

print("o valore de delta", delta)

x1= (-b + delta**0.5) / (2*a) 

print("o valor da primeira raiz é:", x1)

x2= (-b - delta**0.5) / (2*a) 

print("o valor da primeira raiz é:", x2)

#Outros dados para a, b ,c

a = 2
b = 16
c = 3

delta = b**2 - 4*a*c

print("o valore de delta", delta)

x1= (-b + delta**0.5) / (2*a) 

print("o valor da primeira raiz é:", x1)

x2= (-b - delta**0.5) / (2*a) 

print("o valor da primeira raiz é:", x2)



#-------------------------------------------------------------------------------------------------------------------------------

"""
Exercício 2: anos bissextos
Elabore um programa em Python que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão 
lógica que indica se um ano é ou não bissexto. 
Um ano é bissexto se ele é múltiplo de quatro. No entanto, anos múltiplos de 
100 que não são múltiplos de 400 não são bissextos. 
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

"""

ano = float(input("Informe um ano:"))
print((ano % 4 == 0) and (ano % 100 != 0 ) or (ano % 400 == 0))



#print(ano % 4 != 0 )
#print("esse ano não é bissexto")