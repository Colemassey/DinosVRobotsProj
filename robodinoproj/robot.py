from weapon import Weapon
from dino import Dinosaur

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon_one = Weapon("Sword", 10)
        self.weapon_two = Weapon("Laser", 15)
        self.weapon_three = Weapon("Mortar", 30)
        
    def attack(self, dinosaur, dino_list):
        dinosaur.health -= self.weapon_one.attack
        print()
        print(f'Dinosaur {dinosaur.name} was attacked by robot {self.name} and did {self.weapon_one.attack} damge')
        print(f'{dinosaur.name} has {dinosaur.health} remaining health')
        print()
        if dinosaur.health <= 0:
            dino_list.remove(dinosaur)