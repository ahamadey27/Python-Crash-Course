import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion: 
    """Overall class to manage game assets and behaviors"""
    
    def __init__(self):
        """Initiliaze game and create game resources"""
        pygame.init() #initializes background settings that pygame needs to work
        self.clock = pygame.time.Clock() #creates clock for franme rate
        self.settings = Settings() #create instanse of the settings class
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        #self.screen is a surface where game elements can be displayed and pygame.display.set_mode is entire game window
        pygame.display.set_caption('Alien Invasion')
        
        self.ship = Ship(self)
        
        #Sets background color
        #self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Starts the main loops for the game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get(): #event is action that the user perfroms during game play
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #Redraw screen during each pass of the loop. fill method takes one argument: color
            self.screen.fill(self.settings.bg_color) 
            self.ship.blitme()
                    
            #Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60) #set clock (frame rate) to 60 frames per second (tick takes one argument that sets frame rate)
            
if __name__ == '__main__': 
    #Make game instance and run game
    ai = AlienInvasion()
    ai.run_game()

        