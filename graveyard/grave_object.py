import pygame

class Grave_object:
    def __init__(self, x, y, type):
        """
        Graveyard object as tree, tombstone, skeleton etc.
        @param x: x-coordinate
        @param y: y-coordinate
        @param type: name of the object
        """
        self.x = x
        self.y = y

        if type >= 1 and type <=4:
            self.type = 'bone'
            if type == 1:
                self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Bone_1.png')
            elif type == 2:
                self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Bone_2.png')
            elif type == 3:
                self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Bone_3.png')
            elif type == 4:
                self.img = pygame.image.load('GraveyardTilesetNew/png/Tiles/Bone_4.png')
        elif type == 5:
            self.type = 'bush'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/Bush_1.png')
        elif type == 6:
            self.type = 'bush'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/Bush_2.png')
        elif type == 7:
            self.type = 'dead_bush'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/DeadBush.png')
        elif type == 8:
            self.type = 'arrow_sign'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/ArrowSign_1.png')
        elif type == 9:
            self.type = 'tree'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/Tree.png')
        elif type == 10:
            self.type = 'tombstone'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/TombStone_1.png')
        elif type == 11:
            self.type = 'tombstone'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/TombStone_2.png')
        elif type == 12:
            self.type = 'sign'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/Sign_1.png')
        elif type == 13:
            self.type = 'crate'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/Crate.png')
        elif type == 14:
            self.type = 'skeleton'
            self.img = pygame.image.load('GraveyardTilesetNew/png/Objects/Skeleton.png')

    def show(self, game_display):
        """
        Shows the graveyard object
        @param game_display: pygame.game_display
        """
        game_display.blit(self.img, (self.x, self.y))

