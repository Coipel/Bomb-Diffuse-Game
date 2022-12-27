import random
import sys

from wire_module import WireModule

class Bomb():
    def __init__(self, time_limit_sec=None, strike_limit=3):
        self.time_limit_sec = time_limit_sec
        self.strike_limit = strike_limit
        self.strike_count = 0
        
        if self.time_limit_sec == None:
            print("This bomb has no time limit")
        else:
            print(f"This bomb has a time limit of: {self.time_limit_sec} seconds")
            
            
    def setup_modules(self, module_amount: int):
        """ Here all the modules on the bomb are setup at the same time (syncs their start time)"""
        
        self.modules = [None]*module_amount
        module_names = [None]*module_amount
        module_names = [random.choice(['wire module', 'module type 2', 'module type 3']) for _ in range(module_amount)] # Only wire module exists for now the other two are used for proof of concept
        for index in range(module_amount):
            if module_names[index] == 'wire module':
                self.modules[index] = WireModule(index)
            if module_names[index] == 'module type 2':
                self.modules[index] = WireModule(index) # Place holder, in reality would be a different module
            if module_names[index] == 'module type 3':
                self.modules[index] = WireModule(index) # Place holder, in reality would be a different module


    def play(self):
        for module in self.modules:
            module.play(self.time_limit_sec) # All bomb modules will need a self.play() method so this loop is simplied as such
            
            if module.time_left == False:
                print("You have blown up") # [TODO] A GUI display should report this and maybe an explosion image
                break
            if module.module_status == None: # [TODO] Should add a button/menu system instead of using the close window button for both progressing or closing the game
                print("You have closed the game")
                sys.exit()
            
            self.strike_count += int(not module.module_status)
            print(f"Strikes: {self.strike_count}")

            if self.strike_count == self.strike_limit:
                print("Too many strikes you blew up") # [TODO] A GUI display should report this and maybe an explosion image
                break

        print("You disarmed the bomb")