import pygame
from graveyard.tile import Tile
from graveyard.grave_object import Grave_object


class Tile_block(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, type):
        super().__init__()
        """
        Block crated from Tile(s)
        @param init_x: x-coordinate
        @param init_y: y-coordinate
        @param type: tile_block
        """
        self.x = init_x
        self.y = init_y
        self.type = type  # Based on type a tile block is created
        self.block = self.create_block()
        self.width = self.get_width()
        self.height = self.get_height()
        self.pos = (init_x, init_y)
        self.rect = self.get_rect()
        self.type = 'tile_block'  # For next actions, we need to know that this is a tile_block

    def get_rect(self):
        buffer = pygame.Rect((self.x, self.y), (self.width, self.height))
        buffer.update(self.x+5, self.y-60, self.width-55, self.height/4)
        return buffer

    def create_block(self):
        """
        Creates a tile block based on type
        @return: tile block
        """
        if self.type == 0:
            return self.create_ground()
        elif self.type == 1:
            return self.create_block_1()
        elif self.type == 2:
            return self.create_block_2_a()
        elif self.type == 3:
            return self.create_block_2_b()
        elif self.type == 4:
            return self.create_block_3()
        elif self.type == 5:
            return self.create_block_4()
        elif self.type == 6:
            return self.create_block_5()


    def get_width(self):
        """
        Return width of the image of the tile
        @return:
        """
        width = 0
        for tile in self.block:
            width += tile.img.get_width()
        return width

    def get_height(self):
        """
        Return width of the image of the tile
        @return:
        """
        height = 0
        for tile in self.block:
            height += tile.img.get_height()
        return height


    def create_block_1(self):
        """
        Creates a tile block from tiles
        @return: tile block
        """
        tile_1 = Tile(self.x, self.y, 2)
        tile_2 = Tile(tile_1.x, tile_1.y + tile_1.img.get_height(), 9)
        tile_3 = Tile(tile_1.x + tile_1.img.get_width(), tile_1.y, 3)
        tile_4 = Tile(tile_1.x + tile_1.img.get_width(), tile_3.y + tile_3.img.get_height(), 13)

        tb = [tile_1, tile_2, tile_3, tile_4]

        return  tb

    def create_block_2_a(self):
        """
        Creates a tile block from tiles
        @return: tile block
        """
        tile_1 = Tile(self.x, self.y, 15)
        tile_2 = Tile(tile_1.x + tile_1.img.get_width(), tile_1.y, 15)
        tile_3 = Tile(tile_2.x + tile_1.img.get_width(), tile_2.y, 16)

        return [tile_1, tile_2, tile_3]

    def create_block_2_b(self):
        """
        Creates a tile block from tiles
        @return: tile block
        """
        tile_1 = Tile(self.x, self.y, 14)
        tile_2 = Tile(tile_1.x + tile_1.img.get_width(), tile_1.y, 16)

        return [tile_1, tile_2]

    def create_block_3(self, no = 4):
        """
        Creates a tile block from tiles
        @param no: number of middle tiles
        @return: tile block
        """
        block = [Tile(self.x, self.y, 14)]
        for i in range(no):
            block.append(Tile(block[len(block)-1].x + block[len(block)-1].img.get_width(), block[len(block)-1].y, 15))

        return block

    def create_block_4(self):
        """
        Creates a tile block from tiles
        @return: tile block
        """
        tile_1 = Tile(self.x, self.y, 14)
        tile_2 = Tile(tile_1.x + tile_1.img.get_width(), tile_1.y, 15)
        tile_3 = Tile(tile_2.x + tile_2.img.get_width(), tile_2.y, 16)

        return [tile_1, tile_2, tile_3]

    def create_block_5(self):
        """
        Creates a tile block from tiles
        @return: tile block
        """
        block = self.create_block_3(no=3)

        block.append(Tile(block[len(block) - 1].x + block[len(block) - 1].img.get_width(), block[len(block) - 1].y, 16))

        return block

    def create_ground(self):
        """
        Creates the main tile block (ground shape)
        @return: tile block
        """
        block = []

        block.append(Tile(self.x, self.y, 2))

        for i in range(9):
            block.append(Tile(block[len(block)-1].x + block[len(block)-1].img.get_width(), block[len(block)-1].y, 2))

        block.append(Tile(block[len(block)-1].x + block[len(block)-1].img.get_width(), block[len(block)-1].y, 8))
        block_up_1_i =len(block)-1

        for i in range(1):
            block.append(Tile(block[len(block)-1].x + block[len(block)-1].img.get_width(), block[len(block)-1].y, 5))

        block.append(Tile(block[len(block) - 1].x + block[len(block) - 1].img.get_width(), block[len(block) - 1].y, 10))

        for i in range(4):
            block.append(Tile(block[len(block)-1].x + block[len(block)-1].img.get_width(), block[len(block)-1].y, 2))

        block.append(Tile(block[block_up_1_i].x, block[block_up_1_i].y - block[block_up_1_i].img.get_height(), 4))
        block_up_11 = len(block)-1
        block.append(Tile(block[len(block)-1].x + block[len(block)-1].img.get_width(), block[len(block)-1].y, 5))
        block_up_12 = len(block)-1
        block.append(Tile(block[len(block) - 1].x + block[len(block) - 1].img.get_width(), block[len(block) - 1].y, 6))
        block_up_13 = len(block)-1
        block.append(Tile(block[block_up_11].x, block[block_up_11].y - block[block_up_11].img.get_height(), 1))
        block.append(Tile(block[block_up_12].x, block[block_up_12].y - block[block_up_12].img.get_height(), 2))
        block.append(Tile(block[block_up_13].x, block[block_up_13].y - block[block_up_13].img.get_height(), 3))
        return block

    def show(self, game_display):
        """
        Shows the tile block
        @param game_display: pygame.game_display
        """
        for pg_object in self.block:
            pg_object.show(game_display)
