from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self): # use run_game to call your other methods you create in battlefield
        self.display_welcome()
        self.battle()
        pass

    def display_welcome(self):
        print(f"Let's start a Battle!")
        pass
    

    def battle(self):
        game_end = False
        round_counter = 1
        while game_end == False:
            if self.herd.dinos.health or self.fleet.robots.health >= 1:
                self.robot_turn()
                self.dino_turn()
                print(f"Round {round_counter} is over")
                round_counter = +1
                return
            
            elif self.herd.dinos.health or self.fleet.robots.health <= 0:
                game_end == True
                self.show_winners()
                break

        pass

    def dino_turn(self):
        self.show_dino_options()
        dino_index = int(input("Select a dinosaur to attack with"))
        self.robot_show_options()
        robot_index = int(input("Select a robot to attack"))
        self.herd.dinos[dino_index].attack(self.fleet.robots[robot_index])
        pass

    def robot_turn(self):
        self.robot_show_options()
        robot_index = int(input("Select a robot to attack with"))
        self.show_dino_options()
        dino_index = int(input("Select a dino to attack"))
        self.fleet.robots[robot_index].attack(self.herd.dinos[dino_index])
        pass

    def show_dino_options(self):
        print('Current Dino Herd')
        index = 0
        for dino in self.herd.dinos:
            print(f'Press {index} to select {dino.name} ({dino.health} health)')
            index += 1
        pass

    def robot_show_options(self):
        print("Current Robot Fleet")
        index = 0
        for robot in self.fleet.robots:
            print(f'Press {index} to select {robot.name} ({robot.health} health)')
            index += 1
        pass

    def show_winners(self):
        print(f"battle over")
        pass

    # finish UML from battlefield list