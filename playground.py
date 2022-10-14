import pygame
from hero import Hero
from wraith import Wraith
from reaper import Reaper
from scarecrow import Scarecrow
from graveyard.tile_block import Tile_block
from graveyard.grave_object import Grave_object


class Playground:
    def __init__(self):
        """
        Constructor
        """
        self.width = 1920
        self.height = 1080
        self.background = pygame.image.load('background/PNG/2_game_background/2_game_background.png')
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.playground = self.create_playground()

        self.hero_1 = Hero(110,60,self.collision_sprites,0,500,60)
        self.ghost = Wraith(110,60,self.collision_sprites,2,500,60)
        self.scarecrow = Scarecrow(110,60,self.collision_sprites,2,50,60)
        self.reaper = Reaper(110,60,self.collision_sprites,2,1400,60)



    def create_playground(self):
        """
        Generates the playground with the tiles and graveyard objects
        """
        my_playground = []

        my_playground.append(Tile_block(0, self.height - 100, 0))  # Ground
        my_playground.append(Tile_block(450, 600, 3))  # Island with dead bushes
        my_playground.append(Tile_block(0, 450, 2))  # I sland on the left
        my_playground.append(Tile_block(500, 300, 6))  # Island in the middle
        my_playground.append(Tile_block(1280, 350, 4))  # Island on the right (top)
        my_playground.append(Tile_block(800, 700, 3))  # Island on the right (middle)
        # Graveyard objects - trees, tombstones, sign arrows, bushes, bones
        my_playground.append(Grave_object(800, 215, 8))
        my_playground.append(Grave_object(500, 65, 9))
        my_playground.append(Grave_object(900, 65, 9))
        my_playground.append(Grave_object(1200, 120, 9))
        my_playground.append(Grave_object(1620, 120, 9))
        my_playground.append(Grave_object(1450, 280, 11))
        my_playground.append(Grave_object(1550, 280, 11))
        my_playground.append(Grave_object(1650, 280, 11))
        my_playground.append(Grave_object(1170, self.height - 205, 13))
        my_playground.append(Grave_object(1400, 800, 1))
        my_playground.append(Grave_object(1350, 900, 3))
        my_playground.append(Grave_object(200, 890, 8))
        my_playground.append(Grave_object(100, 370, 5))
        my_playground.append(Grave_object(10, 410, 14))
        my_playground.append(Grave_object(500, self.height - 160, 6))
        my_playground.append(Grave_object(700, self.height - 160, 6))
        my_playground.append(Grave_object(550, self.height - 180, 5))
        my_playground.append(Grave_object(1400, self.height - 590, 9))
        my_playground.append(Grave_object(1300, self.height - 420, 7))
        my_playground.append(Grave_object(1450, self.height - 405, 10))
        my_playground.append(Grave_object(1700, self.height - 205, 13))
        my_playground.append(Grave_object(550, self.height - 570, 12))
        my_playground.append(Grave_object(600, self.height - 550, 7))
        my_playground.append(Grave_object(450, self.height - 550, 7))


        return my_playground

    def show_playground(self, game_display):
        """
        Display plaground
        @param game_display: gpygame.display
        """
        self.hero_1.show(game_display)
        self.ghost.show(game_display)
        self.scarecrow.show(game_display)
        self.reaper.show(game_display)

        for my_obj in self.playground:
            my_obj.show(game_display)


    def run(self, enemy_types):
        """
        Main loop of the application
        @param enemy_types:
        """
        clock = pygame.time.Clock()
        pygame.init()
        game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Halloween Party')

        self.ghost.collision_hero.append(self.hero_1)
        self.reaper.collision_hero.append(self.hero_1)


        for my_obj in self.playground:
            if isinstance(my_obj,Tile_block):
                self.hero_1.collision_sprites.add(my_obj)
                self.ghost.collision_sprites.add(my_obj)
                self.scarecrow.collision_sprites.add(my_obj)
                self.reaper.collision_sprites.add(my_obj)

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            game_display.blit(self.background, [0, 0])  # Display background
            self.show_playground(game_display)  # Show playground

            self.hero_1.update()
            self.reaper.update()
            self.ghost.update()
            self.scarecrow.update()
            self.hero_1.collision_enemy.clear()
            self.hero_1.collision_enemy.append(self.ghost)
            self.hero_1.collision_enemy.append(self.scarecrow)
            self.hero_1.collision_enemy.append(self.reaper)

            pygame.display.update()  # Update of the screen

            clock.tick(60)


if __name__ == '__main__':
    enemy_types = [3, 2, 4, 5]
    pg = Playground()
    pg.run(enemy_types)
