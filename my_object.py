import pygame
import numpy as np
import pygame.gfxdraw
from pygame.math import Vector2

class My_Object:
    def __init__(self, screen_width, screen_height, type, x=None, y=None):
        self.size_x = screen_width
        self.size_y = screen_height
        self.pos_x = x
        self.pos_y = y
        self.type = type
        self.health = 100
        self.gravity = 0.8
        self.invisible = False



    def lower_hp(self):
        self.health -= 5




