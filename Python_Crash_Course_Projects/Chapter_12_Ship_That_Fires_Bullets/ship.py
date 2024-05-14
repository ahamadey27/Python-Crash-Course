import pygame

class Ship():
    """A class to manage the main character ship"""
    
    def __init__(self, ai_game): #ai_game = instance of the AlienInvasion class
        """initliaze shit and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image and get its react
        self.image = pygame.image.load('C:\Users\hamad\Documents\GitHub\Python-Crash-Course\Python_Crash_Course_Projects\Chapter_12_Ship_That_Fires_Bullets\images\ship.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom 
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)