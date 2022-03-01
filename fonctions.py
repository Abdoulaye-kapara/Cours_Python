"""def welcome():
    print("Welcome ")
    nombre1 = int(input("entrez le premier nombre :"))
    nombre2 = int(input("entrez le second nombre :"))
    resultat = nombre1 / nombre2
    if resultat < 1:
        print("le nombre {} est superieur au nombre 1".format(nombre2))
    else:
        print("le nombre {} est superieur au nombre 2".format(nombre1))
    
welcome()

def next_year():
    global year
    print("fin de l'annee :", year)
    year += 1
    print("debut de l'annee :", year)

year = 2018
next_year()
next_year()

def addition():
    resultat = 5 + 5
    return resultat
print("le resultat de l'addition est : ", addition()) 

def multiply() :
     return 5 * 8
print("le resultat de la multiplication est : ", multiply())

def max(a, b):
    if a > b:
        return a
    else:
        return b
first_value = int(input("entrez la valeur de a : "))
second_value = int(input("entrez la valeur de b : "))
print("la valeur max est :", max(first_value, second_value))"""

def get_vowels_numbers(word):
    nb_vowels = 0
    for letter in word :
        if letter in ['a', 'e', 'i', 'u', 'o', 'y', 'A', 'E', 'I', 'U', 'O', 'Y'] :
            nb_vowels += 1
    return nb_vowels
word = input("Entrer  un mot :")
vowels_count = get_vowels_numbers(word)
print("Il y a ", vowels_count, "voyelles dans le mot", word)

