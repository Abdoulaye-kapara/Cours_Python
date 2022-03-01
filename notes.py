import statistics
from statistics import mean
from random import shuffle 

#creer une liste des notes et calculer la moyenne avec la fonction mean
"""notes = [8, 12, 10, 9, 4, 20, 14, 3]
print(notes)
resultat = statistics.mean(notes)
#resultat = mean(notes)
print("la moyenne de l'eleve est {}".format(resultat))
shuffle(notes)
print(notes)"""
 #recuperer les donnees siasies et les transformées en liste

"""text = input("Enter une chaine de la forme (email-pseudo-password)").split("-")
print(text)
print("salue {}, ton email : {}, ton password : {}".format(text[1], text[0], text[2]))"""


#exo video4
"""generateur = input("entrez les mots de la forme (mot1/mot2/mot3)").split("/")
print(generateur)
shuffle(generateur)
print(generateur)
length_generateur = len(generateur)
print(length_generateur)
if length_generateur < 10:
    print(generateur[0], generateur[1])
if 10 <= length_generateur:
    print(generateur[length_generateur -1], generateur[length_generateur -2], generateur[length_generateur -3])"""

#exo video 5
#la boucle for
"""for num_client in range(1, 6):
    print("vous etes le client N°", num_client)
#pour les emails
emails = ['aliou@game.com','ousmane@dev.com', 'kapara@gmail.com', 'abdullah@hotmail.fr', 'kapara@yahoo.fr']
blacklist = ['aliou@game.com','ousmane@dev.com']
for email in emails:
    if email in blacklist :
        print("Email {} interdit ! envoie impossible".format(email))
        continue
    print("Email envoyé à :",email)"""
#la boucle while
#salarié 1500$ /mois
#salary = 1500

#tant que salaire < 2000$, +120$
#while salary <  2000:
    #ajouter 120$ au salaire
   # salary += 120
    #print("votre salaire est de ", salary, "$")

"""#exercice sur la boucle while : un youtubeur "diallo" a 2500 abonnees
inscription = 2500
#il gagne 10% d'audience supplementaire chaque moi
months = 0
#on souhaite estimer, combien aura t'il apres 2ans 
while months <= 24:
    #l'audience augmente de 10%
    inscription *= 1.10
    print("Vous avez actuellement {} abonnees".format(inscription))
    months += 1"""
#exo video 5
nombre = float(input("entrez un nombre"))
prix = 500
while  0 < nombre < 1000:
    #print("entrer un nouveau nombre ")
    nombre = float(input("entrez un nombre"))
    if nombre == prix:
        print("bravo vous avez trouve le juste prix")
    else:
        if nombre < prix :
            print("moins")   
        else:
            print("plus") 
        print("vous avez perdu")
    break 



 


