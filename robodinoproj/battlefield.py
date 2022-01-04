from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self): # use run_game to call your other methods you create in battlefield
        self.display_welcome()
        pass

    def display_welcome(self):
        pass

    # finish UML from battlefield list