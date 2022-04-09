import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__() # нужен для спрайтов
        self.screen = ai_game.screen # обращение к экрану
        self.settings = ai_game.settings # обращение к настройкам
        self.collor = self.settings.bullet_color # цвет пули, который указан в настройках
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # используем rect для спавна прямоугольника в координате 0, 0 с заданной высотой и шириной, которые в настройках
        self.rect.midbottom = ai_game.ship.rect.midtop #совместил верхний центр корабля со снарядом
        self.y = float(self.rect.y) # позиция снаряда

    def update(self): # обновление позиции снаряда
        self.y -=self.settings.bullet_speed_fact# начальная позиция - скорость указанная в настройках
        self.rect.y = self.y # заменяем значение/ обновление позиции снаряда


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.collor, self.rect) # вывод снаряда на экран в определенном цвете


