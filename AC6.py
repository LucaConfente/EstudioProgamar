"""
beecrowd 1000
"""
print("Hello World!")


"""
beecrowd 1001
"""

numero1 = int(input(""))
numero2 = int(input(""))

soma = (numero1 + numero2)
print("X =", soma)



"""
beecrowd 1010

codigo1 = int(input("Informe o código da peça1:"))
numero1 = int(input("Informe o número de peças1:"))
valor1 = float(input("Informe o valor unitário da peça1:"))


codigo2 = int(input("Informe o código da peça2:"))
numero2 = int(input("Informe o número de peças2:"))
valor2 = float(input("Informe o valor unitário da peça2:"))
"""

codigo1, numero1, valor1 = input().split()
codigo1 = int(codigo1)
numero1 = int(numero1)
valor1 = float(valor1)

codigo2, numero2, valor2= input().split()
codigo2 = int(codigo2)
numero2 = int(numero2)
valor2 = float(valor2)

valor_pagar = (numero1 * valor1) + (numero2 * valor2)
valor_pagar = "{:.2f}".format(valor_pagar)
print("VALOR A PAGAR: R$", valor_pagar,)

"""
beecrowd 1013

"""

(a, b, c) = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a+b + abs(a-b)) / 2

MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) / 2
MaiorABC = "{:.0f}".format(MaiorABC)
print(MaiorABC, "eh o maior")



"""
beecrowd 1015
"""
x1, y1 = input().split()

x2, y2 = input().split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

Distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

Distancia = "{:.4f}".format(Distancia)

print(Distancia)