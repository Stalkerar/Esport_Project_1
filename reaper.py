import pygame,glob
import numpy as np
from pygame.math import Vector2
from my_object import My_Object

class Reaper(My_Object):
    def __init__(self, screen_width, screen_height, collision_sprites, type, x=None, y=None):
        super().__init__(screen_width, screen_height, type, x=None, y=None)

        self.pos = (x, y)
        self.size = (self.size_x, self.size_y)
        self.direction = Vector2()
        self.direction.x = -1
        self.speed = 5
        self.rect = self.get_rect()
        self.collision_hero = []
        self.image = pygame.image.load('reaper_3/Idle/0_Reaper_Man_Idle Blinking_000.png')
        self.collision_sprites = pygame.sprite.Group()
        self.on_floor = False
        self.gravity = 0.8
        self.see_hero = False

        self.anim_death_speed = 10
        self.anim_death = glob.glob('reaper_3/Dying/0_Reaper_Man_Dying_*.png')
        self.anim_death.sort()
        self.anim_death_pos = 0
        self.anim_death_max = len(self.anim_death) - 1

        self.anim_attackingRight_speed = 10
        self.anim_attackingRight = glob.glob('reaper_3/Attacking/0_Reaper_Man_Slashing_*.png')
        self.anim_attackingRight.sort()
        self.anim_attackingRight_pos = 0
        self.anim_attackingRight_max = len(self.anim_attackingRight) - 1

        self.anim_attackingLeft_speed = 10
        self.anim_attackingLeft = glob.glob('reaper_3/Attacking_left/0_Reaper_Man_Slashing_*.png')
        self.anim_attackingLeft.sort()
        self.anim_attackingLeft_pos = 0
        self.anim_attackingLeft_max = len(self.anim_attackingLeft) - 1

        self.anim_runLeft_speed = 10
        self.anim_runLeft = glob.glob('reaper_3/Running_left/0_Reaper_Man_Running_*.png')
        self.anim_runLeft.sort()
        self.anim_runLeft_pos = 0
        self.anim_runLeft_max = len(self.anim_runLeft) - 1

        self.anim_runRight_speed = 10
        self.anim_runRight = glob.glob('reaper_3/Running/0_Reaper_Man_Running_*.png')
        self.anim_runRight.sort()
        self.anim_runRight_pos = 0
        self.anim_runRight_max = len(self.anim_runRight) - 1

        self.anim_idleLeft_speed = 10
        self.anim_idleLeft = glob.glob('reaper_3/Idle_left/0_Reaper_Man_Idle Blinking_*.png')
        self.anim_idleLeft.sort()
        self.anim_idleLeft_pos = 0
        self.anim_idleLeft_max = len(self.anim_idleLeft) - 1

        self.anim_idleRight_speed = 10
        self.anim_idleRight = glob.glob('reaper_3/Idle/0_Reaper_Man_Idle Blinking_*.png')
        self.anim_idleRight.sort()
        self.anim_idleRight_pos = 0
        self.anim_idleRight_max = len(self.anim_idleRight) - 1



    def run_anim_idleleft(self):
        self.anim_idleLeft_speed -= 10
        if self.anim_idleLeft_speed == 0:
            self.image = pygame.image.load(self.anim_idleLeft[self.anim_idleLeft_pos])
            self.anim_idleLeft_speed = 10
            if self.anim_idleLeft_pos == self.anim_idleLeft_max:
                self.anim_idleLeft_pos = 0
            else:
                self.anim_idleLeft_pos += 1

    def run_anim_idleRight(self):
        self.anim_idleRight_speed -= 10
        if self.anim_idleRight_speed == 0:
            self.image = pygame.image.load(self.anim_idleRight[self.anim_idleRight_pos])
            self.anim_idleRight_speed = 10
            if self.anim_idleRight_pos == self.anim_idleRight_max:
                self.anim_idleRight_pos = 0
            else:
                self.anim_idleRight_pos += 1




    def run_anim(self):
        if self.direction.x == -1:
            self.run_anim_left()
        else:
             self.run_anim_right()



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



    def run_anim_death(self):
        self.anim_death_speed -= 10
        if self.anim_death_speed == 0:
            self.image = pygame.image.load(self.anim_death[self.anim_death_pos])
            self.anim_death_speed = 10
            if self.anim_death_pos == self.anim_death_max:
                self.anim_death_pos = self.anim_death_max
            else:
                self.anim_death_pos += 1



    def get_view_rect(self):

            buffer = pygame.Rect(self.pos, (self.size_x + 1200, 40))

            buffer.center = self.pos
            return buffer



    def move_vision(self):
        for sprite in self.collision_sprites.sprites():
            if (sprite.rect.colliderect(self.get_view_rect())):
                self.see_hero = False

        for hero in self.collision_hero:
            if hero.invisible == False:
                 if hero.rect.colliderect(self.get_view_rect()):
                    self.see_hero = True
                 else:
                    self.see_hero = False
            else:
                self.see_hero = False


    def get_rect(self):
        buffer = pygame.Rect(self.pos, (self.size_x, self.size_y+10))
        return buffer

    def show(self, gamedisplay):
        gamedisplay.blit(self.image, self.rect)

    def hunt_horizontal_collision(self):
        dummy = pygame.Rect(1200, 270, 50, 50)
        dummy2 = pygame.Rect(1920, 270, 50, 50)
        if (self.rect.colliderect(dummy2)):
             if (self.rect.right >= dummy2.left and (self.direction.x == 1)):
                self.rect.right = dummy2.left
                self.run_anim_idleRight()

        if (self.rect.colliderect(dummy)):
             if (self.rect.left <= dummy.right and (self.direction.x == -1)):
                 self.rect.left = dummy.right
                 self.run_anim_idleleft()

    def horizontal_collision(self):
        dummy = pygame.Rect(1200, 270, 50, 50)
        dummy2 = pygame.Rect(1920, 270, 50, 50)
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

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.pos = (self.rect.x, self.rect.y)

    def set_hunt(self):
        for hero in self.collision_hero:
            if hero.invisible == False:
                if hero.rect.x < self.rect.x:
                    self.direction.x = -1
                else:
                    self.direction.x = 1
                if hero.rect.colliderect(self.get_rect()):
                    self.run_anim_attack()
                    self.speed = 0
                else:
                    self.speed = 5
            else:
                self.speed = 5
                self.see_hero = False

        self.rect.x += self.direction.x * (self.speed + 5)
        self.pos = (self.rect.x, self.rect.y)





    def update(self):
        self.death()

        if(self.invisible == False):
            self.move_vision()
            self.run_anim()
            if (self.see_hero == True):
                self.set_hunt()
                self.hunt_horizontal_collision()
            else:
                self.move()
                self.horizontal_collision()
        else:
            self.run_anim_death()


        self.apply_gravity()
        self.vertical_collision()

    def death(self):
        if (self.health <= 0):
            self.invisible = True