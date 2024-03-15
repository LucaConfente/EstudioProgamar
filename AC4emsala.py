"""
Desenvolva uma versão inicial de CLI (command-line interface)
para analisar se um aluno foi ou não aprovado em uma disciplina.
A aplicação deve atender aos seguintes requisitos:

A CLI deve perguntar ao usuário o seu nome.
Caso a resposta do usuário seja um texto vazio, o programa deve ser encerrado;
Em seguida, o programa deve calcular a média do usuário.
Para isso, o programa deve ler as notas de AP1, AP2, AS e AC.
Em seguida, deve exibir na tela a média final do aluno. Considere que a média é
calculada como (AP1 + AP2) * 0.4 + AC * 0.2,
sendo que a AS pode substituir a AP1 ou a AP2 (a menor dentre as duas);
Por fim, a aplicação deve exibir na tela se o aluno foi aprovado ou reprovado,
baseado na sua média. A média para aprovação é 7.0.
Organize o seu código em funções com responsabilidades distintas
(uma para o cálculo de nota, uma para exibição de informações, uma para leitura de
dados, etc.). Caso as notas passadas sejam inválidas (menores que 0 ou maiores que 10),
o programa não deve calcular nada e deve ser encerrado.
"""


def ler_nome():
    """Retorna uma string com o nome do aluno."""
    return input("Informe o nome do aluno: ")

def ler_notas():
    """
    Retorna 4 notas das avaliações AP1, AP2, AS e AC, nesta ordem.
    As notas são do tipo float.
    """
    ap1 =  float(input("Informe a nota da sua AP1: "))
    ap2 = float(input("Informe a nota da sua AP2: "))
    ac = float(input("Informe a nota da sua AC: "))
    asub = float(input("Informe a nota da sua Asub: "))
    return ap1, ap2, asub, ac

def notas_sao_validas(ap1, ap2, asub, ac):
    """
    Retorna True se todas as quatro notas estão entre 0 e 10, inclusive.
    Returna False caso contrário.
    """
    if ap1 >= 0 and ap1 <= 10 and ap2 >= 0 and ap2 <= 10 and asub >= 0 and asub <= 10 and ac >= 0 and ac<= 10:
        return True
    else:
        return False



def selecionar_notas(ap1, ap2, asub):

    if ap1 < asub:
        return asub, ap2
    elif ap2 < asub:
        return asub, ap1
    else:
        return ap1, ap2
    """
    Retorna as duas maiores notas, considerando que a AS pode substituir a
    AP1 ou a AP2, aquela que tiver a menor nota. Se a AS for menor que as duas,
    retorna apenas a AP1 e a AP2.
    """

def calcular_media(nota1, nota2, ac):

    return round (nota1 + nota2 * 0.4 + 0.2 * ac, 2)
    """
    Retorna a média da disciplina, arredondada em duas casas decimais.
    M = (AP1 + AP2) * 0.4 + AC * 0.2
    """

def aluno_foi_aprovado(media):
    """
    Retorna True se o aluno foi aprovado, e False caso contrário.
    A média de aprovação é 7.0.
    """
    return media >= 7

def analisar_media(media):
    """
    Exibe a média na tela.
    Exibe se o aluno foi aprovado ou reprovado.
    """
    print(media)
    if aluno_foi_aprovado(media):
        print("Aluno foi aprovado.")
    else:
        print("Aluno foi reprovado.")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            nota1, nota2 = selecionar_notas(ap1, ap2, asub)
            media = calcular_media(nota1, nota2, ac)
            analisar_media(media)

main()