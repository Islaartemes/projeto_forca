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
#   LUAN -                             #
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

    lista_categoria_selecionada = categorias[int(categoria)-1]

    palavra_secreta = lista_categoria_selecionada[randint(0,len(lista_categoria_selecionada)-1)].upper()

    acertou = False
    enforcou = False
    acertos = [ "_" for letra in palavra_secreta ]
    corretas = []
    erradas = []


    while True:    
        print(f"Categoria: {categoria_selecionada}")
        print(boneco[len(erradas)])
        
        
        print("Palavra: " + " ".join (acertos))

        print("Letras Informadas: ")

        print("Corretas: " + ", ".join(corretas))
        
        print("Erradas: " + ", ".join(erradas))

        if "".join(acertos) == palavra_secreta:
            acertou = True
            break

        if len(erradas) == 6:
            enforcou = True
            break

        letra_informada = input("Insira uma letra: ").upper()

        if letra_informada in palavra_secreta:
            corretas.append(letra_informada)
            posicao = 0
            for letra in palavra_secreta:
                if letra_informada == letra:
                    acertos[posicao] = letra_informada
                posicao += 1

        else:
            erradas.append(letra_informada)
