#la boucle for
#afficher hello word 10 fois
#for i in range(0,10):
 #   print("hello word")

#for i in range(0, 15):
#   print("j'ame python")

#exo afficher les nombres pairs compris entre 1 et 30

'''for i in range(1, 31):
    if i % 2 == 0:
        print(i)'''
#demander a l'utilsteur de sair un nombre 10x de suite 
#afficher la somme 

"""somme = 0
for i in range(0, 10):
    nombre = float(input("entrez un nombre : "))
    somme = somme + nombre 
moyenne = somme / 10
print(""somme)
print("la moyenne est :",moyenne)"""
#autrement avec un tableau
'''tab = []
res = 0
for i in range(1, 11):
    phrase = "entrer le nombre" + str(i)+ ":"
    nb = float(input(phrase))
    tab.append(nb)
    
for i in tab:
    # somme
    res += i
# moyenne   
moy = res / len(tab)
print("La somme est: ", res)
print("La moyenne est: ", moy)'''

#demander  l'utilisateur d'entrer un nombre 
#nombre = int(input("entrez un nombre : "))
#for i in range(1, nombre + 1):
#    print(i*"* ")

n = int(input("entrez un nombre : "))
for ligne in range(1, n+1):
    for colonne in range(1, ligne+1):
        print("*", end=" ")
    print("")




