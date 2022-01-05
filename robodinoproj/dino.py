

class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power
    
    def attack_move (self, Robot):
        Robot.health -= self.attack