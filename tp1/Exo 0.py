#exo0
a = 5.3
b = 9.70
c = a+b
print(c)
c += a # qui veut dire C = c+a
print (c)
d = c
print(d)
d-=1 # d= d-1#
print (d)
# à la fin du programme c = 20,3
 # CORRECTION
""" maintenant j'affiche le type de variable de C 
"""
c_type = type(c)  # on récupère le type de c
print(c_type)     # on affiche le type  et c'est un nombre décimale c'est à dire Float

#A l'aide la fonction int(), créer une nouvelle variable c_int qui contient la valeur de la variable c
c_int = int(c)      # int permet d'avoir un nombre entier à partir d'un nombre décimal
print("La valeur entière de c est : ",c_int)
print(type(c_int)) #là on affiche le type de la valeur de c_int
