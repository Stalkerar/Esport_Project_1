import pygame
import numpy as np

class Tile:
    def __init__(self, x, y, type):
        """
        Tile of the playground: ground, islands
        @param x: x-coordinate
        @param y: y-coordinate
        @param type: tile
        """
        self.x = x
        self.y = y
        self.type = 'tile'

        if type == 1:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_1_brown.png')
        if type == 2:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_2_brown.png')
        if type == 3:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_3_brown.png')
        if type == 4:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (4).png')
        if type == 5:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (5).png')
        if type == 6:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (6).png')
        if type == 7:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_7_brown.png')
        if type == 8:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (8).png')
        if type == 9:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (9).png')
        if type == 10:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (10).png')
        if type == 11:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_11_brown.png')
        if type == 12:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (12).png')
        if type == 13:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile (13).png')
        if type == 14:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_14_brown.png')
        if type == 15:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_15_brown.png')
        if type == 16:
            self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Tile_16_brown.png')

    def show(self, game_display):
        game_display.blit(self.img, (self.x, self.y))