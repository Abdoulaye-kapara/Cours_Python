from model.player import player 
from model.weapon import Weapon

knife = Weapon("couteau", 3)

player1 = player("graven", 20, 3)
player1.set_weapon(knife)
#player1.damage(3)
#print("vous possedez desormais", player1.get_health(), "point de vie")
player2 = player("Bob", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("Bienvenue au joueur", player1.get_pseudo(), "/ point de vie", player1.get_health(), "/ Attaque", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), "/ point de vie", player2.get_health(), "/ Attaque", player2.get_attack_value())