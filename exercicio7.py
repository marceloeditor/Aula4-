

aniversariante = input (" aniversariante ? (sim/não) ")
ingresso = input (" Tem ingresso ? (sim/não)" )


if aniversariante == "sim" : 
    aniversariante == True
else :
    aniversariante = False

if ingresso == "sim":
    ingresso = True
else :
    ingresso = False

if aniversariante == True or ingresso == True :
    print ( "Pode entrar ")
else :
    print ( " Acesso negado , compre um ingresso seu caloteiro ")