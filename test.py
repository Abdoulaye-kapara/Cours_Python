
#print(var)
#recuperer un variable 
#prenom = input("entrer votre nom") 

#exercice4

#prenom = input("entrer votre prenom :")
#nom = input("entrer votre nom :")
#age= input("entrer votre age :")
#plat_prefere = input("entrer votre plat prefere :")
#Profession = input("entrer votre profession :")

#print(prenom)
#print(nom)
#print(age)
#print(plat_prefere)
#print(Profession)
#print("bienvenue",prenom,nom)

"""val1 = int(input("entrer la valeur 1:"))
val2 = int(input("entrer la valeur 2 :"))
resultat = val1 + val2
resultat2 = val1 - val2
resultat3 = val1 * val2
resultat4 = val1 / val2
resultat5 = val1 % val2

print(val1)
print(val2)

print("la somme des deux valeur est :", resultat )
print("la soustraction des deux valeur est :", resultat2 )
print("la multiplication des deux valeur est :", resultat3 )
print("la dision  des deux valeur est :", resultat4 )
print("la modulo des deux valeur est :", resultat5 )"""

#exercice 7: entrer la longueur et la largeur et calculer l'aire du rectangle 

"""
L = float(input("entrer la longueur:"))
l = float(input("entrer la largeur:"))
A = L * l 

print(" La longueur est de ", L)
print ("la largeur est de ", l)
print ("AIRE est de ", A)
"""
#exercice 8  calculer l'aire d'un disque en demandant le rayon 
"""rayon = float(input("entrer le rayon du disque :"))
Aire = rayon * rayon* 3.14
print ("l'aire du disque est  ", Aire)"""

"""
#exercice 8: demander l'utilisateur de saisir le perimetreet la largeur 
# calculer l'aire et la longueur et afficher les valeurs 

l= float(input("entrer la largeur du rectangle:"))
P = float(input("entrer le perimetre :"))
L = ((P / 2) - l)
Aire = L * l
print ("la longueur est  ", L)
print ("l'aire du rectangle est  ", Aire)"""

#exercice 9: operateur de comparaison ( <>, <=, =>, ==, =|) 
#recuperer l'age de A et B ensuite dite si l'age 
"""age1 = int(input("entrer l'age 1 :"))
age2 = int(input("entrer l'age 2 :"))

resultat = (age1 > age2) 
print("l'age 1 est superieur a age2  ", resultat)
resultat = (age1 < age2) 
print("l'age 1 est inferieur a age2  ", resultat)
resultat = (age1 == age2) 
print("l'age 1 est eagal a age2  ", resultat)
resultat = (age1 != age2) 
print("l'age 1 est different a age2  ", resultat)"""

#Les conditions 
#exercice 1 demander a l'utilisateur d'entrer l'age et d'afficher sil est majeur 
'''age = int(input("entrer l'age  :"))
#if age > 18 :
 #   print("la personne est majeur ")
if age < 18 and age > 12 :
    print("la personne est un adolescent ")
else :
    print(" la personne est soit un enfant ou un adulte ")'''

"""# verifications de la longueur d'une chaine de caractere 
password = input("Entre votre mot de passe : ")
password_length = len(password)
#verifion si le mot de passe est superieur a 8
if password_length <= 8:
    print("le mot de passe est trop court ")
elif 8 < password_length <= 12:
    print("le ùot de passe est moyen ")
else:
    print("le mot de passe est parfait  ")"""

#exercice sur les places du cinema 
"""age = int(input("Entrez votre age:  "))
total_mineur = 7
total_majeur = 12
if age >= 18:
    print("le prix de votre entrer est de : {}$".format(total_majeur))
else:
    print("le prix de votre entrer est de : {}$".format(total_mineur))

popcorn = input("Voulez -vous du popcorn ? ")
if popcorn == "oui":
    total_majeur += 5
    total_mineur += 5
    if age >= 18:
        print("le prix total de votre entrer est de :{}$".format(total_majeur))
    else:
        print("le prix total de votre entrer est de :{}$".format(total_mineur))
else:
    if age >= 18:
        print("Le total de votre ticket est: {}$".format(total_majeur))
    else:
        print("Le total de votre ticket est: {}$".format(total_mineur))"""


        #execice 10
"""nombre1 = float(input("Entrez le premier nombre:  "))
nombre2 = float(input("Entrez le dexieme  nombre:  "))
resultat = nombre1 + nombre2
print("le resultat de l'addition est :",resultat)
resultat = nombre1 - nombre2
print("le resultat de la soustraction est :",resultat)
resultat = nombre1 / nombre2
print("le resultat de la division est :",resultat)
resultat = nombre1 * nombre2
print("le resultat de la multiplication est :",resultat)"""

#exo 
'''nombre = float(input("Entrez un nombre:  "))
resultat = nombre % 2
if resultat == 0 :
    print("le nombre est paire ")
else :
    print("le nombre est impair")'''


"""#exo 
nombre1 = float(input("Entrez le premier nombre:  "))
nombre2 = float(input("Entrez le dexieme  nombre:  "))

signe = input("choisir une operation (+,-,*,/)")
if signe == '+':
    resultat = nombre1 + nombre2
    print("le resultat de l'addition est : ",resultat)
if signe == "-" :
    resultat = nombre1 - nombre2
    print("le resultat de la soustraction est : ",resultat)
if signe == "*" :
    resultat = nombre1 * nombre2
    print("le resultat de la multiplication est : ",resultat)
if signe == "/" :
    if nombre2 == 0 :
        print("impossible de diviser")
    else :
        resultat = nombre1 / nombre2
        print("le resultat de la division est : ",resultat)"""
#exo1
"""age= int(input("Entrez votre age: "))
if age < 18 :
    print("la personne est mineur")
else:
    print("la personee est majeur ")"""

#exo if elif else

"""nombre1 = float(input("Entrez le premier nombre:  "))
nombre2 = float(input("Entrez le dexieme  nombre:  "))

signe = input("choisir une operation (+,-,*,/)")
if signe == '+':
    resultat = nombre1 + nombre2
    print("le resultat de l'addition est : ",resultat)
elif signe == "-" :
    resultat = nombre1 - nombre2
    print("le resultat de la soustraction est : ",resultat)
elif signe == "*" :
    resultat = nombre1 * nombre2
    print("le resultat de la multiplication est : ",resultat)
elif signe == "/" :
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        print("le resultat de la division est : ",resultat)
    else:
        print("la division est impossible")
else:
    print("vous devez obligatoirement faire un choix")"""

#les tableaux
"""notes = [12,15.7,20,40.5,90]
somme = notes[0] + notes[1] + notes[2] + notes[3] + notes[4]
moyenne = somme / 5
print("la somme est : ",somme)
print("la moyenne est : ",moyenne)
taille = len(notes)
print("la derniere note et : ", notes[taille-1])
print("la premiere note est : ", notes[taille-taille])"""

#exercices sur les tableaux

"""notes = [16,28,15,13.75,17,7]
taille = len(notes)
dernierelem = notes[taille-1]
print(dernierelem)
if dernierelem % 2 != 0:
    notes[0] = 12
    somme = notes[0] + notes[1]
    print(notes)
    print("la somme est :",somme)
else:
    multiplication = notes[0] * 7
    print("la multiplication est :",multiplication)"""

#TD_Listes
#online_players = ["graven", "Anana", "Cleymax", "bob"]
"""print(online_players)
print(online_players[1])
print(online_players[len(online_players) -1])"""
# modifier 'graven' -- 'gravenilvec'
"""online_players[0] = "gravenilvec"
print(online_players)
online_players[2:4] = ["papi", "mami"]
#on imagine qu'un joueur "Gameur123" se connecte
online_players.append("Gameur123")
#pour supprimer une valeur dans la liste 
#del online_players[1]
online_players.pop(1)
online_players.clear()
print(online_players)"""

"""nombre = float(input("entrer un nombre"))
table = []
somme = nombre + nombre
star = nombre * nombre
carre = nombre * nombre
table.append(nombre)
table.append(somme)
table.append(star)
table.append(carre)
#table.append([nombre, somme, star, carre])
print("le tableau est :",table)"""

#utilisations de pop() & remove and del
notes = [12, "papa", "ananas", 18, 17, "malien", 15.50]
print(notes)
#notes.pop(1)
#notes.pop(1)
#notes.pop(3)
"""notes.remove("papa")
notes.remove("ananas")
notes.remove("malien")"""
del notes[0]
del notes[2]
del notes[2]
del notes[3]
print("le tableau nettoyer sans les nombres :", notes)