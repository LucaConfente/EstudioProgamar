"""
AC5

Pesquise sobre o módulo random, em particular sobre a função randint() (veja aqui a documentação oficial). 
Entendendo como essa função é utilizada, elabore um jogo por CLI e que você controla um aventureiro e está lutando contra um monstro.
Considere os seguintes requisitos:

O aventureiro possui uma vida inicial igual a 100, seu ataque é um valor aleatório entre 10 e 20, 
e sua defesa é um valor aleatório entre 1 e 5;
O monstro possui uma vida aleatória entre 60 e 80, seu ataque é um valor aleatório entre 20 e 30, e não possui defesa;
Após a definição dos atributos do aventureiro e do monstro, o programa deve exibir os atributos iniciais e 
em seguida rodar um loop até que a vida de um dos dois fique igual ou abaixo de zero;
No loop, considere as seguintes ações:
O programa escreve o número da rodada do combate;
O aventureiro ataca o monstro, reduzindo da vida do monstro um valor aleatório entre 1 e o ataque do aventureiro;
Se a vida do monstro ficar igual ou abaixo de zero, o programa deve escrever na tela que o monstro morreu e encerrar o loop;
Em seguida, o monstro ataca o aventureiro, reduzindo da vida deste um valor aleatório entre 1 e o ataque do monstro, 
menos a defesa do aventureiro;
Se a vida do aventureiro ficar igual ou abaixo de zero, o programa deve escrever na tela que o aventureiro morreu e encerrar o loop;
Por fim, o programa deve escrever os atributos do aventureiro e do monstro.
O programa não deve possuir inputs do usuário, ele apenas deve exibir as informações. 

Faça o exercício em uma única função, main().
"""


import random

def main():
 ################## AVENTUREIRO #####################

    aventureiro_vida = 100
    print("A vida do aventureiro é 100")
 
    aventureiro_ataque = random.randint(10, 20)
    print("O ataque do aventureiro é:", aventureiro_ataque)

    aventureiro_defesa = random.randint(1, 5)
    print("A defesa do aventureiro é:", aventureiro_defesa)
    

####################### MONSTRO #########################

    monstro_vida = random.randint(60, 80)
    print("A vida do monstro é:", monstro_vida)

    monstro_ataque = random.randint(20, 30)
    print("O ataque do monstro é:", monstro_ataque)

    i = 0 #Mudar numero da Rodada

    while (aventureiro_vida > 0) and (monstro_vida > 0):

        i = i + 1

        monstro_vida = monstro_vida - random.randint(1, aventureiro_ataque)

        if monstro_vida <= 0:
            print("O monstro morreu!") 
            
        else:
            dano_monstro = random.randint(1 ,monstro_ataque) - aventureiro_defesa

            if dano_monstro <= 0:
                aventureiro_vida - 1 # Para o aventureiro sempre tomar no minimo um dano

            else:
                aventureiro_vida = aventureiro_vida - random.randint(1 ,monstro_ataque)

            if aventureiro_vida <= 0:
                print("O aventureiro morreu!")

            else:
                print("")
                print("Rodada", i)
                print("Aventureiro: Vida", aventureiro_vida, "- att", aventureiro_ataque, "- def", aventureiro_defesa)
                print("Monstro: Vida", monstro_vida, "- att", monstro_ataque)
                
                
main()