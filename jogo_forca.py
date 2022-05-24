from random import randint

menu = """
>>>>>>>>>>>>     UNIESP     <<<<<<<<<<<<
#       INTRODUÇÃO A PROGRAMAÇÃO       #
#                                      #
#              CATEGORIA               #     
#       1- FRUTA                       #
#       2- ANIMAL                      #
#       3- PAÍS                        #
#       DIGITE OUTRA TECLA PARA SAIR   #
#                                      #
#                                      #
#   GRUPO:                             #
#   ISLA - islaartemes@gmail.com       #
#   GABRIELA -                         #
#   GUSTAVO -                          #
#   LUAN -  luanlucas.r10@hotmail.com  #
#   Mª ALICE -                         #
########################################

"""

opcao_jogo = "1"

categorias = [
    ["abacaxi", "abacate", "amora", "banana", "bacuri", "buriti", "caju", "carambola", "cacau", "damasco", "figo", "framboesa", "goiaba", "graviola", "jambo", "jabuticaba", "kiwi", "laranja", "nectarina", "seriguela"],
    ["abelha","abutre","albatroz","alce","alpaca","anaconda","anchova","andorinha","anta","aranha","arara","asno","atum","avestruz","bacalhau","bacuri","badejo","bagre","baiacu","baleia","barata","barbo","cabra","cachalote","cachorro","camelo","camundongo","canguru","dinossauro","doninha","dourado","elefante","gafanhoto","gaivota","galinha","hadoque","hamster","iguana","iguanara","impala","jabiru","jabuti"],
    ["Alemanha","Andorra","Angola","Argentina","Barbados","Belize","Benim","Bielorrússia","Cabo Verde","Camarões","Camboja","Chile","China","Dinamarca","Egito","Equador","Filipinas","Guiana","Holanda","Iraque","Irlanda","Jamaica","Portugal","Turquia","Uruguai"]
]

boneco = [
    """
    ##################
##              ##
##              ##
##          ##########
##
##
##
##
##
##
##
    """, 
    """
    ##################
##              ##
##              ##
##          ##########
##            *****
##           *     *
##           *     *
##           *     *
##            *****
##
##
##
##
##
##
    """,
    """
    ##################
##              ##
##              ##
##          ##########
##            *****
##           *     *
##           *     *
##           *     *
##            *****
##              *
##            *****
##              *
##              *
##              *
##              *
    """,
    """
    ##################
##              ##
##              ##
##          ##########
##            *****
##           *     *
##           *     *
##           *     *
##            *****
##              *
##            *****
##           *  *
##          *   *
##              *
##              *
    """,
    """
    ##################
##              ##
##              ##
##          ##########
##            *****
##           *     *
##           *     *
##           *     *
##            *****
##              *
##            *****
##           *  *  *
##          *   *   *
##              *
##              *
    """,
    """
    ##################
##              ##
##              ##
##          ##########
##            *****
##           *     *
##           *     *
##           *     *
##            *****
##              *
##            *****
##           *  *  *
##          *   *   *
##              *
##              *
              *****
             *
            *
    """,
    """
    ##################
##              ##
##              ##
##          ##########
##            *****
##           *     *
##           *     *
##           *     *
##            *****
##              *
##            *****
##           *  *  *
##          *   *   *
##              *
##              *
              *****
             *     *
            *       *
    """


]

while True:

    if opcao_jogo == "1":
        print(menu)
        categoria = input("Escolha a categoria: ")
        categoria_selecionada = ""
        
        if (categoria == "1"):
            categoria_selecionada = "Fruta"
        elif (categoria == "2"):
            categoria_selecionada = "Animal"
        elif (categoria == "3"):
            categoria_selecionada = "País"
        else:
            print("Jogo encerrado!")
            break