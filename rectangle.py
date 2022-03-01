class Rectangle :
    def __init__(self, Longueur, Largeur):
        self.Longueur = Longueur
        self.Largeur = Largeur 

monrectangle = Rectangle(15,10)
Aire = monrectangle.Longueur * monrectangle.Largeur
perimetre = (monrectangle.Longueur + monrectangle.Largeur) * 2
print("le perimetre du rectange est :", perimetre)
print("L'aire du rectangle est :", Aire)
