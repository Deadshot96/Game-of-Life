import pygame
import random
from settings import *

class Grid:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.xoff = X_OFF
        self.yoff = Y_OFF
        self.gameWinWidth = GAMEWIN_WIDTH
        self.gameWinHeight = GAMEWIN_HEIGHT
        self.rows = ROWS
        self.cols = COLS
        self.fps = FPS
        self.clock = None
        self.font = None
        self.grid = None
        self.win = None
        self.gameWin = None

        
    def grid_init(self):
        pygame.init()
        pygame.font.init()
        
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        
        self.gameWin = self.win.subsurface((self.xoff, self.yoff, self.gameWinWidth, self.gameWinHeight))
        
        self.win.fill((30, 20, 50))
        self.gameWin.fill((40, 102, 139))
        
        pygame.display.update()
    
    def close(self):
        pygame.font.quit()
        pygame.quit()
    
    def draw(self):
        pass
    
    def run(self):
        if not pygame.display.init():
            self.grid_init()
            
        run = True
        while run:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                    
                    
        self.close()
    
    
if __name__ == "__main__":
    print("Hello, World!")
    X = Grid()
    X.run()
