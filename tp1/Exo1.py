#Ecrire un algorithme qui demande un nombre à l'utilisateur puis affiche le carré de ce nombre
print("Saisir un nombre:") # Print permet de demander qqch à un utilisateur (sur l'interface du site)
valeur_saisie = input() # je stocke la valeur saisie dans une variable
nombre = float(valeur_saisie) # je transforme cette valeur en nombre décimal

squared = nombre * nombre  # je calcule carré de nombre

print("Le carré de", nombre, " est ", squared)  # j'affiche le résultat