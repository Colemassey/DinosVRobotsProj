from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.show_winners()
        pass

    def display_welcome(self):
        print(f"Let's start a Battle!")
        pass
    

    def battle(self):
        while len(self.fleet.robots) > 0 and len(self.herd.dinos) > 0:
            self.robot_turn()
            if len(self.herd.dinos) == 0:
                pass
            else:
                self.dino_turn()
        

    def dino_turn(self):
        self.show_dino_options()
        dino_index = int(input("Select a dinosaur to attack with"))
        self.robot_show_options()
        robot_index = int(input("Select a robot to attack"))
        self.herd.dinos[dino_index].attack_move(self.fleet.robots[robot_index], self.fleet.robots)
        pass

    def robot_turn(self):
        self.robot_show_options()
        robot_index = int(input("Select a robot to attack with"))
        self.show_dino_options()
        dino_index = int(input("Select a dino to attack"))
        self.fleet.robots[robot_index].attack(self.herd.dinos[dino_index], self.herd.dinos)
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

    def show_winners(self):# if robo list length = 0 then dino wins else print robots win
        if len(self.fleet.robots) == 0:
            print(f"")
            print(f"The Dinosaur Herd WINS!")
        else:
            print("")
            print(f"The Robot Fleet WINS!")
        print(f"battle over")
        pass

    # finish UML from battlefield list