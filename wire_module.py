import random

class WireModule:
    def __init__(self, module_id: int):
        self.module_id = module_id
        self.wire_slots = 5 # This can be made variable in the future, but this will complicate rule making for a first prototype
        
    def generate_wire_types(self):
        self.wire_types = ['empty']*self.wire_slots
        for index in range(self.wire_slots):
            self.wire_types[index] = random.choice(['blue', 'red', 'green'])


    def print_module_start(self, spacing, length):
        print("\n"*spacing)
        print("-"*length + "Wire-Module" + "-"*length)
    

    def print_module_end(self, spacing, length):
        print("-"*length + "Wire-Module" + "-"*length)
        print("\n"*spacing)


    def print_module_details(self):
        print("You are viewing Wire Module #" + str(self.module_id))
        print("This Wire Module contains " + str(self.wire_slots) + " wire slots")
        print("Wires: " + str(self.wire_types))
        

    def rulebase(self):
        """ Method used to hold and apply the rules to generate what are the correct cuts to make """
        self.correct_cuts = [0]*self.wire_slots
        blues = self.wire_types.count('blue')
        reds = self.wire_types.count('red')
        greens = self.wire_types.count('green')
          
        # [NOTE] For now there must be 5 wire_slots and no wire can be missing (this simplifies making rules)
        if blues == 1:                  # If there is one blue wire, cut the fourth wire
            self.correct_cuts[3] = 1
        if blues == 2:                  # If there is two blue wires, cut the second wire
            self.correct_cuts[1] = 1
        if reds >= 4:                   # If four red wires or more, cut the second wire
            self.correct_cuts[0] = 1
        if greens == 3:
            self.correct_cuts[2] = 1    # If three green wires, cut the third wire
        if greens == 1:
            self.correct_cuts[4] = 1    # If one green wire, cut the fifth wire


    def print_rules(self):
        """ Method used to print in English the rules established for Wire Modules in the rulebase() method """
        print("-----Wire-Module-Instructions-----")
        
        print("*Don't cut unless specified*")

        print("---BLUE WIRES---")
        print("~If one blue wire, cut the fourth wire~")
        print("~If two blue wires, cut the second wire~")
        
        print("---RED WIRES---")
        print("~If four red wires or more, cut the first wire~")

        print("---GREEN WIRES---")
        print("~If three green wires, cut the third wire~")
        print("~If one green wire, cut the fifth wire~")


    def userinput_console(self):
        prompt = "Input your answers as a binary number (ex: 01010) [1: cut, 0: no cut]\n"
        self.user_cuts = list(map(int, list(input(prompt)))) # input: string -> list of character numbers -> list of integers
        module_outcome = self.user_cuts == self.correct_cuts

        print("Inputted Cuts: " + str(self.user_cuts)) 
        print("Correct Cuts: " + str(self.correct_cuts))
        print("Matched: " + str(module_outcome))

        if module_outcome == True:
            print("Sucessfully disarmed Wire Module #" + str(self.module_id))
        else:
            print("Failed to disarmed Wire Module #" + str(self.module_id))
        
        return module_outcome


    def play(self):
        self.print_module_start(1,25)
        self.generate_wire_types()
        self.print_module_details()
        self.rulebase()
        self.print_rules()
        module_outcome = self.userinput_console()
        self.print_module_end(1,25)

        return module_outcome


if __name__ == '__main__':
     wire_module_1 = WireModule(1)
     wire_module_1_outcome = wire_module_1.play()
     print(wire_module_1_outcome)