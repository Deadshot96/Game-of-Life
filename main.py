import pygame
import random
from settings import *
from colors import *
from cell import Cell
from pygame import Surface
from typing import Tuple

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
        self.evolveFlag = False
        self.counter = 0
        self.genPerSec = GENPERSEC

        
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
        self.clear_grid()
        
        for row in self.grid:
            for cell in row:
                if random.random() < 0.25:
                    cell.regen()
                    
    def clear_grid(self):
        for row in self.grid:
            for cell in row:
                cell.kill()
                    
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
        color = SIENNA
        for i in range(self.cols + 1):
            pygame.draw.line(win, color, (0, i * self.size), (self.gameWinWidth, i * self.size), lineWidth)
            pygame.draw.line(win, color, (i * self.size, 0), (i * self.size, self.gameWinHeight), lineWidth)
            
            
    def get_row_col(self, x: int, y: int) -> Tuple[int]:
        x -= self.xoff
        y -= self.yoff
        
        return y // self.size, x // self.size
    
    def is_valid_dims(self, row: int, col: int) -> bool:
        return row in range(self.rows) and col in range(self.cols)
    
    def get_alive_neighbours(self, row, col) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                r = (row + i + self.rows) % self.rows
                c = (col + j + self.cols) % self.cols
                count += (1 if self.grid[r][c].is_alive() else 0)
                
        count -= (1 if self.grid[row][col].is_alive() else 0)
        return count
    
    def run(self):
        if not pygame.display.init():
            self.grid_init()
            
        run = True
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    
                    if keys[pygame.K_r]:
                        self.randomize_grid()
                        self.evolveFlag = False
                        self.counter = 0
                    
                    if keys[pygame.K_c]:
                        self.clear_grid()
                        self.evolveFlag = False
                        self.counter = 0
                        
                    if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                        self.evolveFlag = True
                        self.counter = 0
                    
                    if keys[pygame.K_ESCAPE]:
                        self.evolveFlag = False
                        self.counter = 0
                        
            pressed = pygame.mouse.get_pressed()
            
            if pressed[0]:
                x, y = pygame.mouse.get_pos()
                row, col = self.get_row_col(x, y)
                
                if self.is_valid_dims(row, col):
                    # print(row, col, sep="\t")
                    self.grid[row][col].regen()
                    
            if self.evolveFlag:
                if self.counter == 0:
                    for row in self.grid:
                        for cell in row:
                            r, c = cell.get_dims()
                            alive = self.get_alive_neighbours(r, c)
                            
                            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                            # Any live cell with two or three live neighbours lives on to the next generation.
                            # Any live cell with more than three live neighbours dies, as if by overpopulation.
                            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                                
                            if not cell.is_alive() and alive == 3:
                                cell.regen()
                            if cell.is_alive() and alive < 2 or alive > 3:
                                cell.kill()
                
                self.counter += 1
                if self.counter == (self.fps // self.genPerSec):
                    self.counter = 0
                

            self.draw()
            
        self.close()
    
    
if __name__ == "__main__":
    print("Hello, World!")
    X = Grid()
    X.run()
