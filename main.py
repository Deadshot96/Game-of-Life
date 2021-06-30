import pygame
import random
from settings import *
from colors import *
from cell import Cell
from pygame import Surface

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
        self.size = RES
        self.clock = None
        self.titleFont = None
        self.grid = None
        self.win = None
        self.gameWin = None
        self.gameWinRect = None

        
    def grid_init(self):
        pygame.init()
        pygame.font.init()
        
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        
        self.gameWinRect = pygame.Rect(self.xoff, self.yoff, self.gameWinWidth, self.gameWinHeight)
        self.gameWin = self.win.subsurface(self.gameWinRect)
        
        self.win.fill(MID_BLACK)
        self.gameWin.fill(BLACK)
        
        self.titleFont = pygame.font.SysFont(TITLE_FONT, FONT_SIZE)
        title = self.titleFont.render("Game of Life", 1, GOLD)
        w, h = title.get_size()
        blitX = (self.width - w) // 2
        blitY = (self.yoff - h) // 2
        self.win.blit(title, (blitX, blitY))
    
        # Create Grid
        self.create_grid()
        self.randomize_grid()
    
        self.clock = pygame.time.Clock()
        pygame.display.update()
        
        
        
    def create_grid(self):
        if not self.grid:
            self.grid = list()
        self.grid.clear()
        for row in range(self.rows):
            self.grid.append(list())
            for col in range(self.cols):
                self.grid[row].append(Cell(row, col))

    def randomize_grid(self):
        for row in self.grid:
            for cell in row:
                if random.random() < 0.25:
                    cell.regen()
                    
    def draw_grid(self, win: Surface):
        for row in self.grid:
            for cell in row:
                cell.draw(win)
    
    def close(self):
        pygame.font.quit()
        pygame.quit()
    
    def draw(self):
        self.draw_grid(self.gameWin)
        self.draw_lines(self.gameWin)
        
        pygame.display.update()

    def draw_lines(self, win: Surface):
        lineWidth = 2
        for i in range(self.cols + 1):
            pygame.draw.line(win, WHITE, (0, i * self.size), (self.gameWinWidth, i * self.size), lineWidth)
            pygame.draw.line(win, WHITE, (i * self.size, 0), (i * self.size, self.gameWinHeight), lineWidth)
    
    def run(self):
        if not pygame.display.init():
            self.grid_init()
            
        run = True
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            self.draw()
                    
                    
        self.close()
    
    
if __name__ == "__main__":
    print("Hello, World!")
    X = Grid()
    X.run()
