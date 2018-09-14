import pygame
from pygame.locals import *
import time
from pygame.locals import *
import random


class HeroPlane(object):
    def __init__(self,screen):
        self.x = 190
        self.y = 476
        self.name = './feiji/hero1.png'
        self.image = pygame.image.load(self.name)
        self.bullets = []
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for x in self.bullets:
            x.display()
            x.move_bullet()
        # 创建临时列表，存放当y<0是要删除的子弹
        tmp = []
        for x in self.bullets:
            if x.y < 0:
                tmp.append(x)
        for y in tmp:
            self.bullets.remove(y)

    def move_left(self):
        if self.x >= 10:
            self.x -= 10
        else:
            self.x = self.x

    def move_right(self):
        if self.x <= 380:
            self.x += 10
        else:
            self.x = self.x

    def move_up(self):
        if self.y >= 10:
            self.y -= 10
        else:
            self.y = self.y

    def move_down(self):
        if self.y <= 466:
            self.y += 10
        else:
            self.y = self.y

    def biubiu_bullet(self):
        bullet = HeroBullet(self.screen, self.x, self.y)
        self.bullets.append(bullet)

  # 创建英雄子弹


class HeroBullet(object):
    def __init__(self,screen, plane_x, plane_y):
        self.x = plane_x + 39
        self.y = plane_y - 22
        self.name = './feiji/bullet.png'
        self.image = pygame.image.load(self.name)
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


    def move_bullet(self):
        self.y = self.y - 10


class Enemy(object):
    def __init__(self, screen):
        self.num = 5
        self.screen = screen
        self.x = [random.randint(0, 429) for p in range(self.num)]
        self.y = [0, 0, 0, 0, 0]
        self.bullet = []
        self.name = './feiji/enemy0.png'
        self.image = pygame.image.load(self.name)
        self.direction = 'right'
        self.ori = 'down'

    def display(self):
        i = 0
        while i <= 4:
            self.screen.blit(self.image, (self.x[i], self.y[i]))
            i = i + 1
        for x in self.bullet:
            x.display()
            x.enemybullet_move()

    def move_enemy(self):
        m = 0
        while m <= 4:
            if self.ori == 'down':
                self.y[m] += 0.5 + m * 0.1
            elif self.ori == 'up':
                self.y[m] -= 0.5 + m * 0.1

            if self.y[m] <= 0:
                self.ori = 'down'
            elif self.y[m] >= 600 - 39:
                self.ori = 'up'

            if self.direction == 'right':
                self.x[m] += 0.5
            elif self.direction == 'left':
                self.x[m] -= 0.5
            if self.x[m] >= 429:
                self.direction = 'left'
            elif self.x[m] <= 0:
                self.direction = 'right'
            m = m + 1

    def soot(self):
        num = random.randint(0, 60)
        if num == 8:
            b = EnemyBullet(self.screen, self.x, self.y)
            self.bullet.append(b)


class EnemyBullet(object):
    def __init__(self,screen,enemyplane_x, enemyplane_y):
        self.screen = screen
        self.x = [x+22 for x in enemyplane_x]
        self.y = [x+40 for x in enemyplane_y]
        self.name = './feiji/bullet1.png'
        self.image = pygame.image.load(self.name)

    def display(self):
        i = 0
        while i <= 4:
            self.screen.blit(self.image, (self.x[i], self.y[i]))
            i = i + 1

    def enemybullet_move(self):
        k = 0
        while k <= 4:
            self.x[k] = self.x[k]
            self.y[k] = self.y[k] + 5
            k = k + 1
    def move(self):
        k = 0
        while k <= 4:
            self.x[k] = self.x[k]
            self.y[k] = self.y[k] + 5
            k = k + 1
        if self.y[k] > 600:
            del self.x[k]
            del self.y[k]








def main():
    # 创建窗口
    screen = pygame.display.set_mode((480,600), 0, 32)
    # 填充背景
    background =pygame.image.load('./feiji/background.png')
    # 填充玩家飞机
    hero = HeroPlane(screen)
    enemy = Enemy(screen)

    while True:
        # 背景在窗口位置
        screen.blit(background, (0, 0))
        # 玩家在窗口位置
        hero.display()
        # 敌人在窗口显示位置
        enemy.display()
        # 敌人飞机开枪
        enemy.soot()

        # 敌人飞机移动
        enemy.move_enemy()
        # 显示出来
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    hero.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    hero.move_right()
                elif event.key == K_w or event.key == K_UP:
                    hero.move_up()
                elif event.key == K_s or event.key == K_DOWN:
                    hero.move_down()
                elif event.key == K_SPACE:
                    hero.biubiu_bullet()


    # time.sleep(600)
if __name__== '__main__':
    main()

