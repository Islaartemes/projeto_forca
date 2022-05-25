from ast import While
import time
from random import randint


menu = """
\033[1;44m>>>>>>>>>>>>>>>>      UNIESP     <<<<<<<<<<<<<<<<<\033[m
\033[1;105m#       INTRODUÇÃO A PROGRAMAÇÃO - P1.A          #\033[m
\033[1;46m#                                                #\033[m
\033[1;46m#   CATEGORIAS:                                  #\033[m     
\033[1;46m#     1- FRUTA                                   #\033[m  
\033[1;46m#     2- ANIMAL                                  #\033[m  
\033[1;46m#     3- PAÍS                                    #\033[m  
\033[1;46m#     0- SAIR DO JOGO                            #\033[m  
\033[1;46m#                                                #\033[m  
\033[1;105m#                                                #\033[m  
\033[1;105m#   GRUPO ['A-Z']:                               #\033[m   
\033[1;105m#   ERYCK - eryck.targino3@gmail.com             #\033[m  
\033[1;105m#   GABRIELA - sistemasdagab.i@gmail.com         #\033[m  
\033[1;105m#   GUSTAVO - gustavo.lopes.nobrega@gmail.com    #\033[m
\033[1;105m#   ISLA - islaartemes@gmail.com                 #\033[m 
\033[1;105m#   LUAN - luanlucas.r10@hotmail.com             #\033[m  
\033[1;105m#   Mª ALICE - mariaalice6999@gmail.com          #\033[m
\033[1;105m#                                                #\033[m  
\033[1;44m##################################################\033[m  

\033[;1mSEJA BEM VINDX À FORCA! QUE TAL PASSAR O TEMPO JOGANDO UM POUCO?\033[m
VOCÊ TEM 06 CHANCES PARA DESCOBRIR A PALAVRA SECRETA, ELA ESTÁ RELACIONADA AO TEMA DA CATEGORIA QUE VOCÊ ESCOLHER, SENDO ELAS: \n    > FRUTAS - 1 \n    > ANIMAIS - 2 \n    > PAÍS - 3 \n\n    > SAIR DO JOGO! - 0 \n 

============ AGORA VAMOS COMEÇAR!!!! ============

"""

opcao_jogo = "1"

categorias = [
    ["abacaxi", "abacate", "amora", "banana", "bacuri", "buriti", "caju", "carambola", "cacau", "damasco", "figo", "framboesa", "goiaba", "graviola", "jambo", "jabuticaba", "kiwi", "laranja", "nectarina", "seriguela"],
    ["abelha","abutre","albatroz","alce","alpaca","anaconda","anchova","andorinha","anta","aranha","arara","asno","atum","avestruz","bacalhau","bacuri","badejo","bagre","baiacu","baleia","barata","barbo","cabra","cachalote","cachorro","camelo","camundongo","canguru","dinossauro","doninha","dourado","elefante","gafanhoto","gaivota","galinha","hadoque","hamster","iguana","iguanara","impala","jabiru","jabuti"],
    ["Alemanha","Andorra","Angola","Argentina","Barbados","Belize","Benim","Bielorrússia","Cabo Verde","Camarões","Camboja","Chile","China","Dinamarca","Egito","Equador","Filipinas","Guiana","Holanda","Iraque","Irlanda","Jamaica","Portugal","Turquia","Uruguai"]
]

alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

boneco = [
    """


######################
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

           \033[1;43mCHANCES = 06\033[m

    """, 
    """


######################
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

           \033[1;43mCHANCES = 05\033[m

    """,
    """


######################
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

           \033[1;43mCHANCES = 04\033[m
           
    """,
    """


######################
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

           \033[1;43mCHANCES = 03\033[m

    """,
    """


######################
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

           \033[1;43mCHANCES = 02\033[m

    """,
    """


######################
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
            
           \033[1;43mCHANCES = 01\033[m

    """,
    """


######################
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

           \033[1;41mCHANCES = 00\033[m

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
        elif (categoria == "0"):
            print("\033[1;36mVOCÊ SAIU DO JOGO!\033[m")
            break
        else:
            print("\033[1;33mOPÇÃO INVÁLIDA!\nTENTE NOVAMENTE!\033[m")
            time.sleep(1)
            continue

    lista_categoria_selecionada = categorias[int(categoria)-1]

    palavra_secreta = lista_categoria_selecionada[randint(0,len(lista_categoria_selecionada)-1)].upper()

    acertou = False
    enforcou = False
    acertos = [ "_" for letra in palavra_secreta ]
    corretas = []
    erradas = []
    caracteresNulos = []


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

        if letra_informada not in alfabeto:
            print("\033[1;31mOPÇÃO INVÁLIDA! TENTE OUTRO CARACTERE.\033[m")
            time.sleep(2)

        if letra_informada in corretas or letra_informada in erradas:
            print("\033[1;91mOPÇÃO JÁ UTILIZADA. TENTE OUTRA LETRA!\033[m")
            time.sleep(3)
            continue   
            
        if letra_informada in palavra_secreta:
            corretas.append(letra_informada)
            posicao = 0
            for letra in palavra_secreta:
                if letra_informada == letra:
                    acertos[posicao] = letra_informada
                posicao += 1
  

        elif letra_informada not in alfabeto:
                caracteresNulos.append(letra_informada)

        else:
                erradas.append(letra_informada) 
    

    if acertou:
        print("\033[1;32mVOCÊ VENCEU!!! PARABÉNS!\033[m")
        

    if enforcou: 
        print("\033[1;31mVOCÊ PERDEU! A PALAVRA SECRETA ERA: \033[m"+ palavra_secreta)   
        

    print(

        """
        \033[1;35mQUE TAL JOGAR NOVAMENTE?
        PARA JOGAR NOVAMENTE INSIRA QUALQUER OUTRA TECLA.\033[m
        """
    )
    
    opcao_jogo = input()