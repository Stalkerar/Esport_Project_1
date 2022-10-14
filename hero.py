import pygame, glob
from pygame.math import Vector2
from my_object import My_Object
from scarecrow import Scarecrow
from wraith import Wraith


class Hero(My_Object):
    def __init__(self,screen_width, screen_height,collision_sprites, type, x=None, y=None):
        super().__init__(screen_width, screen_height, type, x=None, y=None)
        self.attacking_state = False
        self.pos = (x,y)
        self.size = (screen_width,screen_height)
        self.rect = self.get_rect()
        self.direction = Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jumpspeed = 16
        self.collision_enemy = []
        self.collision_sprites = pygame.sprite.Group()
        self.on_floor = False
        self.anim_run_speed = 10
        self.anim_speed = 10
        self.anim_run = glob.glob('hero/Walking/0_Warrior_Run_*.png')
        self.anim_run.sort()
        self.anim_run_pos = 0
        self.anim_run_max = len(self.anim_run)-1
        self.hit_timer = 20
        self.anim = glob.glob('hero/Idle/0_Warrior_Idle Blinking_*.png')
        self.anim.sort()
        self.anim_pos = 0
        self.anim_max = len(self.anim)-1


        self.anim_hitted_speed = 20
        self.anim_hitted = glob.glob('hero/Hurt/0_Warrior_Hurt_*.png')
        self.anim_hitted.sort()
        self.anim_hitted_pos = 0
        self.anim_hitted_max = len(self.anim_hitted) - 1


        self.anim_death_speed = 10
        self.anim_death = glob.glob('hero/Dying/0_Warrior_Died_*.png')
        self.anim_death.sort()
        self.anim_death_pos = 0
        self.anim_death_max = len(self.anim_death) - 1

        self.anim_attack_speed = 10
        self.anim_attack = glob.glob('hero/Attacking/0_Warrior_Attack_2_*.png')
        self.anim_attack.sort()
        self.anim_attack_pos = 0
        self.anim_attack_max = len(self.anim_attack) - 1

        self.invisible = False



        self.image = pygame.image.load(self.anim[0])

    def get_rect(self):
        buffer = pygame.Rect((self.pos), (self.size))
        return buffer


    def run_death(self):
        if(self.health <= 0):
            self.invisible = True
            self.speed = 0



    def input(self):
        if(self.invisible == False):
            keys = pygame.key.get_pressed()
            if(keys):
               # self.run_anim_run()
                if keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                elif keys[pygame.K_LEFT]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_UP]:
                    if(self.on_floor):
                        self.direction.y = -self.jumpspeed-5.5

                if keys[pygame.K_SPACE]:
                    self.attacking_state = True
        else:
            self.run_anim_death()




    def got_hit(self):
        for enemy in self.collision_enemy:
            if enemy.invisible == False:
                if (self.rect.colliderect(enemy)):
                    if isinstance(enemy, Scarecrow) or isinstance(enemy, Wraith):
                        if self.invisible == False:
                            enemy.hero_inRange = True
                    if (self.hit_timer != 0):
                        self.hit_timer -= 1
                    else:
                        self.health -= 5
                        self.run_anim_hitted()
                        self.hit_timer = 20


    def attack(self):
        for enemy in self.collision_enemy:
            if(self.rect.colliderect(enemy.get_rect())):
                enemy.lower_hp()
                print(enemy.health)

        self.attacking_state = False


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.run_death()
        self.input()
        if (self.invisible == False):
            if(self.direction.x == 0):
               self.run_anim_idle()
            else:
               self.run_anim_run()

            if self.attacking_state == True:
                self.attack()
                self.run_anim_attack()
            self.got_hit()

        self.rect.x += self.direction.x * self.speed
        self.horizontal_collision()
        self.apply_gravity()
        self.vertical_collision()

    def run_anim_run(self):
        self.anim_run_speed -= 10
        if self.anim_run_speed == 0:
            self.image = pygame.image.load(self.anim_run[self.anim_run_pos])
            self.anim_run_speed = 10
            if self.anim_run_pos == self.anim_run_max:
                self.anim_run_pos = 0
            else:
                self.anim_run_pos += 1

    def run_anim_hitted(self):
        self.anim_hitted_speed -= 20
        if self.anim_hitted_speed == 0:
            self.image = pygame.image.load(self.anim_hitted[self.anim_hitted_pos])
            self.anim_hitted_speed = 20
            if self.anim_hitted_pos == self.anim_hitted_max:
                self.anim_hitted_pos = 0
            else:
                self.anim_hitted_pos += 1

    def run_anim_attack(self):
        self.anim_attack_speed -= 10
        if self.anim_attack_speed == 0:
            self.image = pygame.image.load(self.anim_attack[self.anim_attack_pos])
            self.anim_attack_speed = 10
            if self.anim_attack_pos == self.anim_attack_max:
                self.anim_attack_pos = 0
            else:
                self.anim_attack_pos += 1




    def run_anim_death(self):
        self.anim_death_speed -= 1
        if self.anim_death_speed == 0:
            self.image = pygame.image.load(self.anim_death[self.anim_death_pos])
            self.anim_death_speed = 10
            if self.anim_death_pos == self.anim_death_max:
                self.anim_death_pos = 0
            else:
                self.anim_death_pos += 1



    def run_anim_idle(self):
        self.anim_speed -=2
        if self.anim_speed == 0:
            self.image = pygame.image.load(self.anim[self.anim_pos])
            self.anim_speed = 10
            if self.anim_pos == self.anim_max:
                self.anim_pos = 0
            else:
                self.anim_pos += 1


    def horizontal_collision(self):
        dummy = pygame.Rect(1300,1080 - 405, 1650-1350,405 )
        if(self.rect.colliderect(dummy)):
            if(self.rect.right >= dummy.left and (self.direction.x == 1)):
                self.rect.right = 1300
            if (self.rect.left <= dummy.right and (self.direction.x == -1)):
                self.rect.left = 1300+300


        for sprite in self.collision_sprites.sprites():
            if(self.rect.colliderect(sprite.rect)):
                if(self.rect.right >= sprite.rect.left and (self.direction.x == 1)):
                    self.rect.right = sprite.rect.left

                if(self.rect.left <= sprite.rect.right and (self.direction.x == -1)):
                    self.rect.left = sprite.rect.right


    def vertical_collision(self):
       dummy = pygame.Rect(1300, 1080 - 405, 1650 - 1350, 405)
       if (self.rect.colliderect(dummy)):
           if self.direction.y > 0:
               self.rect.bottom = dummy.top
               self.direction.y = 0
               self.on_floor = True



       for sprite in self.collision_sprites.sprites():
           if(sprite.rect.colliderect(self.rect)):
               if self.direction.y > 0:
                   self.rect.bottom = sprite.rect.top
                   self.direction.y = 0
                   self.on_floor = True
               if self.direction.y < 0:
                   self.rect.top = sprite.rect.bottom
                   self.direction.y = 0
       if self.on_floor and self.direction.y != 0:
         self.on_floor = False


    def show(self,gamedisplay):
       gamedisplay.blit(self.image, self.rect)





