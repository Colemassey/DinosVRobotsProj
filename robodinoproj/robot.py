from weapon import Weapon
from dino import Dinosaur

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon_one = Weapon("Sword", 10)
        self.weapon_two = Weapon("Laser", 15)
        self.weapon_three = Weapon("Mortar", 30)
        #self.storage = ""
        #self.weapon = ""
        #self.weapon_choice()
        
        #weapon = dict[input("sword, laser, bombs")]

    # def weapon_choice(self):
        # could be used to randomly select or have the user select one of the three wepons, i'd save this logic for later
        # pass
    
    #def load_weapon(self, weapon):
        #self.storage.append(weapon)
        #print(f"{weapon.name} has been added to storage")
        #pass
    
    def attack(self, dinosaur): # in battlefield you should be able to code self.fleet.robot_one.attack(dino_one)
        dinosaur.health -= self.weapon_one.attack
        print(f'Dinosaur {dinosaur.name} was attacted by robot {self.name} and did {self.weapon_one.attack} damge')
        print(f'{dinosaur.name} has {dinosaur.health} remaining health')