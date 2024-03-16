"""
AC2
Desenvolva duas funções em Python:

eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau 
no formato ax² + bx + c = 0, supondo as raízes sempre reais;

"""

def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b + delta**0.5) / (2*a) 
    x2 = (-b - delta**0.5) / (2*a) 
    print("o valor da primeira raiz é:", x1)
    print("o valor da primeira raiz é:", x2)


eq_seg_grau(1, -6, 8 )

"""
bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
"""

def bissexto(ano):
    if ((ano % 4 == 0) and (ano % 100 != 0 ) or (ano % 400 == 0)):
        print("Esse ano é bissexto")
    else:
        print("Esse ano não é bissexto")

bissexto(2016)
bissexto(1900)

"""
Exercício 2: salário
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe duas configurações posicionais 
reais, valor_horae num_horas, que exigem ao valor do salário por hora e o número de horas trabalhadas no mês,
respectivamente. Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, 
cujo valor padrão é 0.275. A função retorna o salário líquido de um funcionário, 
calculada como o produto do valor por hora em número de horas, limitado o percentual do imposto de renda dado.
"""
def calcula_salario(valor_horae, num_horas, irpf = 0.275):
    salariobruto = (valor_horae * num_horas) 
    imposto = salariobruto * irpf
    salarioliquido = salariobruto - (salariobruto * irpf)
    print("Seu salário total:", salariobruto)
    print("O imposto a ser pago é:", imposto)
    print("Logo seu salário é:", salarioliquido)

calcula_salario(50, 70)