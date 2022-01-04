from dino import Dinosaur

class Herd:
    
    def __init__(self):
        self.dinos = []
        self.create_herd()

    def create_herd(self): #dino needs name, health, and attack passed in
        dinosaur_one = Dinosaur("Godzilla", 150, 50)
        dinosaur_two = Dinosaur("Barney", 100, 75)
        dinosaur_three = Dinosaur("Bulbasaur", 75, 100)

        self.dinos.append(dinosaur_one)
        self.dinos.append(dinosaur_two)
        self.dinos.append(dinosaur_three)