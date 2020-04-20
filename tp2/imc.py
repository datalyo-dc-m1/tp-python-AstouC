def imc(poids=87,taille=167): #déclaration de la fonction imc#
    '''

    :param poids: le poids de la personne en kg
    :param taille: la taille de la personne en cm
    :return: l'imc de la personne
    '''
    imc=poids/((taille*taille)/100)
    imc=round(imc * 100, 1)
    if imc <= 18.5 : # Pour une condition, j'utilise "if" une fois et lorsque j'ai 3 conditions ou plus, on utilise Elif à la place de "if" à la deuxième ligne#
        print ("vous êtes en maigreur")
    elif imc <= 24.9 :
        print ("vous avez un poids normal")
    elif imc <= 29.9 :
        print ("vous êtes en surpoids")
    elif imc <= 40 :
        print ("vous êtes en obésité")
    else: #aprés chaque deux points, je vais obligatoirement à la ligne
        print ("Vous êtes en obésité massive")
    return imc
print()

mon_imc = imc()
print (mon_imc)
