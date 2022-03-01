age = int(input("entrez votre age :"))
if age <= 0:
    print("age non valide ")
else :
    if age < 8:
        p=5
    elif age <=16:
        p=10
    else:
        p=20
    print("Le prix de votre ticket est de : {} $".format(p))


