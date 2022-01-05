

class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power
    
    def attack_move (self, robot, robot_list):
        robot.health -= self.attack
        print()
        print(f'Dinosaur {robot.name} was attacked by robot {self.name} and did {self.attack} damge')
        print(f'{robot.name} has {robot.health} remaining health')
        print()
        if robot.health <= 0:
            robot_list.remove(robot)