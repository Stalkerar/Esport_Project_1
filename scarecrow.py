from wraith import Wraith
from my_object import My_Object
from pygame.math import Vector2
import pygame,glob


class Scarecrow(My_Object):
    def __init__(self, screen_width, screen_height, collision_sprites, type = None, x=None, y=None):
        super().__init__(screen_width, screen_height, type = None, x=None, y=None)

        self.image = pygame.image.load('scarecrow/Idle/std_0.png')
        self.pos = (x, y)
        self.collision_enemy = []
        self.collision_sprites = pygame.sprite.Group()
        self.rect = self.get_rect()
        self.direction = Vector2()
        self.direction.x = 1
        self.speed = 3
        self.on_floor = False

        self.anim_runLeft_speed = 10
        self.anim_runLeft = glob.glob('scarecrow/Walking_left/walk_*.png')
        self.anim_runLeft.sort()
        self.anim_runLeft_pos = 0
        self.anim_runLeft_max = len(self.anim_runLeft) - 1

        self.anim_runRight_speed = 10
        self.anim_runRight = glob.glob('scarecrow/Walking/walk_*.png')
        self.anim_runRight.sort()
        self.anim_runRight_pos = 0
        self.anim_runRight_max = len(self.anim_runRight) - 1

        self.anim_attackingRight_speed = 10
        self.anim_attackingRight = glob.glob('scarecrow/Attacking/atk_*.png')
        self.anim_attackingRight.sort()
        self.anim_attackingRight_pos = 0
        self.anim_attackingRight_max = len(self.anim_attackingRight) - 1

        self.anim_attackingLeft_speed = 10
        self.anim_attackingLeft = glob.glob('scarecrow/Attacking_left/atk_*.png')
        self.anim_attackingLeft.sort()
        self.anim_attackingLeft_pos = 0
        self.anim_attackingLeft_max = len(self.anim_attackingLeft) - 1

        self.hero_inRange = False



    def run_anim_attack(self):
        if self.direction.x == 1:
            self.run_anim_attackingRight()
        else:
            self.run_anim_attackingLeft()

    def run_anim_attackingRight(self):
        self.anim_attackingRight_speed -= 10
        if self.anim_attackingRight_speed == 0:
            self.image = pygame.image.load(self.anim_attackingRight[self.anim_attackingRight_pos])
            self.anim_attackingRight_speed = 10
            if self.anim_attackingRight_pos == self.anim_attackingRight_max:
                self.anim_attackingRight_pos = 0
            else:
                self.anim_attackingRight_pos += 1


    def run_anim_attackingLeft(self):
        self.anim_attackingLeft_speed -= 10
        if self.anim_attackingLeft_speed == 0:
            self.image = pygame.image.load(self.anim_attackingLeft[self.anim_attackingLeft_pos])
            self.anim_attackingLeft_speed = 10
            if self.anim_attackingLeft_pos == self.anim_attackingLeft_max:
                self.anim_attackingLeft_pos = 0
            else:
                self.anim_attackingLeft_pos += 1



    def run_anim_left(self):
        self.anim_runLeft_speed -= 10
        if self.anim_runLeft_speed == 0:
            self.image = pygame.image.load(self.anim_runLeft[self.anim_runLeft_pos])
            self.anim_runLeft_speed = 10
            if self.anim_runLeft_pos == self.anim_runLeft_max:
                self.anim_runLeft_pos = 0
            else:
                self.anim_runLeft_pos += 1


    def run_anim_right(self):
        self.anim_runRight_speed -= 10
        if self.anim_runRight_speed == 0:
            self.image = pygame.image.load(self.anim_runRight[self.anim_runRight_pos])
            self.anim_runRight_speed = 10
            if self.anim_runRight_pos == self.anim_runRight_max:
                self.anim_runRight_pos = 0
            else:
                self.anim_runRight_pos += 1


    def get_rect(self):
        buffer = pygame.Rect(self.pos, (self.size_x, self.size_y +35))
        return buffer

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.pos = (self.rect.x, self.rect.y)

    def show(self, gamedisplay):
        gamedisplay.blit(self.image, self.rect)



    def run_anim(self):
        if self.direction.x == -1:
            self.run_anim_left()
        else:
             self.run_anim_right()

        if self.hero_inRange == True:
            self.run_anim_attack()

    def update(self):
        self.move()
        self.horizontal_collision()
        self.run_anim()
        self.apply_gravity()
        self.vertical_collision()
        self.hero_inRange = False


    def horizontal_collision(self):
        dummy = pygame.Rect(-70, 360, 50, 50)
        dummy2 = pygame.Rect(360,360, 50, 50)
        if (self.rect.colliderect(dummy2)):
            if (self.rect.right >= dummy2.left and (self.direction.x == 1)):
                self.direction.x = -1

        if (self.rect.colliderect(dummy)):
            if (self.rect.left <= dummy.right and (self.direction.x == -1)):
                self.direction.x = 1


    def vertical_collision(self):
        for sprite in self.collision_sprites.sprites():
            if (sprite.rect.colliderect(self.rect)):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        if self.on_floor and self.direction.y != 0:
            self.on_floor = False


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

