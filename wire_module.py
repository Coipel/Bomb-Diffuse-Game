import random
import pygame

class WireModule:
    def __init__(self, module_id: int, wire_slots = 5):
        self.module_id = module_id
        self.wire_slots = wire_slots # [NOTE] for now it is excepted that this value is equal to 5 (rule making is not a generalized process)

        self.random_wire_types()
        self.rulebase()
        self.user_cuts = [False]*len(self.wire_types)

        self.screen_width = 1200
        self.screen_height = 600
        self.screen_color = 'grey'

        self.wire_length = 400
        self.wire_width = 20
        self.wires_start_horizontal = 100
        self.wires_start_vertical = 100
        self.wires_gap = 100
        self.wire_cut_length = 20

        self.rules_start_horiztonal = 650
        self.rules_start_vertical = 60
        self.rules_gap = 50
        
        self.wire_horizontals = [self.wires_start_horizontal + self.wires_gap*index for (index,_) in enumerate(self.wire_types)]

        self.module_status = None


    def random_wire_types(self):
        self.wire_types = ['empty']*self.wire_slots
        for index in range(self.wire_slots):
            self.wire_types[index] = random.choice(['blue', 'red', 'green'])
    

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


    def draw_cuts(self):
        for (user_cut, wire_horizontal) in zip(self.user_cuts, self.wire_horizontals):
            if user_cut == True:
                pygame.draw.rect(self.screen, self.screen_color, pygame.Rect(wire_horizontal, self.wires_start_vertical + self.wire_length/2 - self.wire_cut_length/2, self.wire_width, self.wire_cut_length))
    

    def draw_led_indictator(self):
        if self.module_status == True:
            pygame.draw.circle(self.screen, 'green', (560,40), 25)
        elif self.module_status == False:
            pygame.draw.circle(self.screen, 'red', (560,40), 25)            
        else:
            pygame.draw.circle(self.screen, 'grey50', (560,40), 25)


    def draw_module(self):
        module_surface = pygame.Surface((self.screen_width, self.screen_height))
        module_surface.fill(self.screen_color) 
        self.screen.blit(module_surface, (0,0))
        
        font = pygame.font.Font(None, 35)
        rules = ["-----Wire-Module-Instructions-----", "*Don't cut unless specified*", "---BLUE WIRES---", "~If one blue wire, cut the fourth wire~",
                        "~If two blue wires, cut the second wire~", "---RED WIRES---", "~If four red wires or more, cut the first wire~",
                        "---GREEN WIRES---", "~If three green wires, cut the third wire~", "~If one green wire, cut the fifth wire~"]
        for (index, rule) in enumerate(rules):
            surface = font.render(rule, True, 'black')
            self.screen.blit(surface, (self.rules_start_horiztonal, self.rules_start_vertical + self.rules_gap*index))
    
        pygame.draw.rect(self.screen, 'grey50', pygame.Rect(80, self.wires_start_vertical-25, 450, 50)) # Top port rectangle
        pygame.draw.rect(self.screen, 'grey50', pygame.Rect(80, self.wires_start_vertical+375, 450, 50)) # Bottom port rectangle

        # Draws the wires and the ports they connect to on the wire module
        for (wire, wire_horizontal) in zip(self.wire_types, self.wire_horizontals):
            pygame.draw.rect(self.screen, wire, pygame.Rect(wire_horizontal, self.wires_start_vertical, self.wire_width, self.wire_length)) # Wires
            pygame.draw.circle(self.screen, 'black', (wire_horizontal + self.wire_width/2, self.wires_start_vertical), 15) # Top ports
            pygame.draw.circle(self.screen, 'black', (wire_horizontal + self.wire_width/2, self.wires_start_vertical + self.wire_length), 15) # Bottom ports


    def userinput(self):
        (mouse_x,_) = pygame.mouse.get_pos()
        mouse_1_pressed = pygame.mouse.get_pressed()[0]
        for (index,_) in enumerate(self.user_cuts):
            # [NOTE] Intentionally does not check the y position since it is not critical
            if mouse_x <= self.wire_horizontals[index] + self.wire_width and mouse_x >= self.wire_horizontals[index] and mouse_1_pressed == True:
                self.user_cuts[index] = True
            if self.user_cuts[index] != self.correct_cuts[index] and self.user_cuts[index] == True:
                self.module_status = False
        if self.user_cuts == self.correct_cuts:
            self.module_status = True


    def play(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(f'Wire Module {self.module_id}')
        
        quit = False
        while quit == False:
            if self.module_status == None: # This prevents from doing more cuts after sucess or failure to disarm wire module
                self.userinput()
            self.draw_module()
            self.draw_cuts()
            self.draw_led_indictator()
        
            pygame.display.update()
            self.clock.tick(15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit = True

        return self.module_status


def main():
    wire_module_1 = WireModule(1) 
    print(wire_module_1.correct_cuts) # For debugging purposes
    wire_module_1_status = wire_module_1.play() # [TODO] To be used in the bomb module to keep track of strikes
    print(wire_module_1_status)


if __name__ == '__main__':
    main()