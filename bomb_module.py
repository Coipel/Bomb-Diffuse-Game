import wire_module as wm

class Bomb():
    def __init__(self, time_limit_minutes=None, strike_limit=3):
        self.time_limit_minutes = time_limit_minutes
        self.strike_limit = strike_limit
        self.strike_count = 0
        
        if self.time_limit_minutes == None:
            print("This bomb has no time limit")
        else:
            print(f"This bomb has a time limit of: {self.time_limit_minutes} minutes")

    def setup_modules(self):
        """ Here all the modules on the bomb are setup """
        self.wire_module_1 = wm.WireModule(1)
        self.wire_module_2 = wm.WireModule(2)
        pass

    def play(self):
        wire_module_1_outcome = self.wire_module_1.play()
        if wire_module_1_outcome == True:
            self.strike_count += 1
            print(f"Strike Count: {self.strike_count}")
        wire_module_2_outcome = self.wire_module_2.play()
        if wire_module_1_outcome == True:
            self.strike_count += 1
            print(f"Strike Count: {self.strike_count}")