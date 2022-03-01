class player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "/ point de vie", health, "/ Attaque", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self) :
        return self.attack

    def damage(self, damage) :
        self.health -= damage
        print("Aie ... vous venez de subir ", damage, "degat")
    
    def attack_player(self, target_player):
        damage = self.attack
        #si le joueur a une arme 
        if self.has_weapon():
            #ajoutons les degats de l'arme au point d'attaque
            damage += self.weapon.get_damage_amount()
        target_player.damage(damage)
    #methode pour changer l'arme du joueur 
    def set_weapon(self, weapon):
        self.weapon = weapon
    #methode pour verifier si le joueur a une arme 
    def has_weapon(self):
        return self.weapon is not None

class Warrior(player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.weapon = None
        self.armor = 3 
        print("Bienvenue au guerrier", pseudo,"/ point de vie", health, "/ Attaque", attack)

    def damage(self, damage) :
        if self.armor > 0 :
            self.armor -= 1
            damage = 0
        super().damage(damage)
        self.health -= damage
        print("Aie ... vous venez de subir ", damage, "degat")
    
    def attack_player(self, target_player):
        damage = self.attack
        #si le joueur a une arme 
        if self.has_weapon():
            #ajoutons les degats de l'arme au point d'attaque
            damage += self.weapon.get_damage_amount()
        target_player.damage(damage)
    #methode pour changer l'arme du joueur 
    def set_weapon(self, weapon):
        self.weapon = weapon
    #methode pour verifier si le joueur a une arme 
    def has_weapon(self):
        return self.weapon is not None
    def blade(self):
        self.armor = 3
        print ("les points d'armure on ete recharger ")
    def get_armor_point(self):
        return self.armor
warrior = Warrior("Darkwarrior", 30, 4)
warrior.damage(4)
print("vie :", warrior.get_health(), "armure:", warrior.get_armor_point())
if issubclass(Warrior, player):
    print("Le guerrier est bien une specialisation de player")
