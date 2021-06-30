import pygame
from pygame import Surface
from settings import *
from typing import Tuple
from colors import *

class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.size = RES
        self.x = self.col * self.size
        self.y = self.row * self.size
        self.currFlag = False
        self.nextFlag = False
        
    def draw(self, win: Surface):
        self.currFlag = self.nextFlag
        rect = self.x, self.y, self.size, self.size
        pygame.draw.rect(win, FLAG_COLOR[self.currFlag], rect)
        
    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col
    
    def get_dims(self) -> Tuple[int]:
        return self.row, self.col
    
    def regen(self) -> None:
        self.nextFlag = True
        
    def kill(self) -> None:
        self.nextFlag = False
        
    def is_alive(self) -> bool:
        return self.currFlag
        
              
    