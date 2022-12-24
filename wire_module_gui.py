import pygame
from sys import exit
import time

class WireModuleGUI:
    def __init__(self, wire_types: list):
        self.wire_types = wire_types
        self.user_cuts = [False]*len(self.wire_types)

        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Wire Module')
        self.screen_color = 'grey'

        self.wire_length = 400
        self.wire_width = 20

        self.wires_start_horizontal = 100
        self.wires_start_vertical = 100
        self.wires_gap = 100
        self.wire_cut_length = 20
        
        self.wire_horizontals = [self.wires_start_horizontal + self.wires_gap*index for (index, _) in enumerate(self.wire_types)]
                
    def draw_cuts(self):
        for (user_cut, wire_horizontal) in zip(self.user_cuts, self.wire_horizontals):
            if user_cut == True:
                pygame.draw.rect(self.screen, self.screen_color, pygame.Rect(wire_horizontal, self.wires_start_vertical + self.wire_length/2 - self.wire_cut_length/2, self.wire_width, self.wire_cut_length))
        
    def draw_led_indictator(self, status=None):
        if status == True:
            pygame.draw.circle(self.screen, 'green', (560,40), 25)
        elif status == False:
            pygame.draw.circle(self.screen, 'red', (560,40), 25)            
        else:
            pygame.draw.circle(self.screen, 'grey50', (560,40), 25)

    def draw_module(self):
        module_surface = pygame.Surface((self.screen_width, self.screen_height))
        module_surface.fill(self.screen_color) 
        self.screen.blit(module_surface, (0,0))
        pygame.draw.rect(self.screen, 'grey50', pygame.Rect(80, self.wires_start_vertical-25, 450, 50)) # Top port rectangle
        pygame.draw.rect(self.screen, 'grey50', pygame.Rect(80, self.wires_start_vertical+375, 450, 50)) # Bottom port rectangle

        # Draws the wires and the ports they connect to on the wire module
        for (wire, wire_horizontal) in zip(self.wire_types, self.wire_horizontals):
            pygame.draw.rect(self.screen, wire, pygame.Rect(wire_horizontal, self.wires_start_vertical, self.wire_width, self.wire_length)) # Wires
            pygame.draw.circle(self.screen, 'black', (wire_horizontal + self.wire_width/2, self.wires_start_vertical), 15) # Top ports
            pygame.draw.circle(self.screen, 'black', (wire_horizontal + self.wire_width/2, self.wires_start_vertical + self.wire_length), 15) # Bottom ports

    def userinput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        (x,_) = pygame.mouse.get_pos()
        s = pygame.mouse.get_pressed()
        #print(x,y,s)

        for (index, _) in enumerate(self.user_cuts):
            if x <= self.wire_horizontals[index] + self.wire_width and x >= self.wire_horizontals[index] and s[0] == True:
                self.user_cuts[index] = True
        
def main():
    time_start = time.time()
    pygame.init()
    clock = pygame.time.Clock()
    wmgui = WireModuleGUI(wire_types)
    while True:
        wmgui.userinput()
        wmgui.draw_module()
        wmgui.draw_cuts()
        wmgui.draw_led_indictator()
        
        time_passed = time.time() - time_start
        #print(f"{time_passed} sec")

        pygame.display.update()
        clock.tick(10)

wire_types = ['green', 'blue', 'blue', 'green', 'red']
main()


    