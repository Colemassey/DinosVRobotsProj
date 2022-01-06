from robot import Robot

class Fleet:
    
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot("WALL-E", 50)
        robot_two = Robot("Terminator", 100)
        robot_three = Robot("Baymax", 75)

        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)




