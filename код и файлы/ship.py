import pygame
from pygame.sprite import Sprite

class Ship(Sprite): # класс корабля
    def __init__(self, ai_game): # ai_game - ссылка на текущую игру
        super().__init__()
        self.screen = ai_game.screen # облегчение обращения к экрану во всех модулях
        self.screen_rect = ai_game.screen.get_rect() # для размещения корабля в нужной позиции
        self.image = pygame.image.load('ship.png') # фото корабля
        self.rect = self.image.get_rect() # вызвана фу-ия get_rect, чтобы позже использовать для позиционирования корабля
        self.rect.midbottom = self.screen_rect.midbottom # расположение корабля внизу по центру
        self.moving_right = False #флаг перемещения
        self.moving_left = False #флаг перемещения
        self.settings = ai_game.settings # для использования в обновлении/скорость корабля
        self.x = float(self.rect.x) # сохранение вещественой/ дробной координаты




    def update(self):  # обновление позиции корабля с учетом флагов
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed_fact
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed_fact
        self.rect.x = self.x # rect хранит только целые числа, переводим в дробь





    def blitme(self):
        self.screen.blit(self.image, self.rect) # выводит изображение на экран в позиции rect

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)