import pygame
fon = pygame.image.load("fon.jpg") # Фон меню



class set:     #класс настроек
    def __init__(self):
        self.screen_width = 1200 #ширина экрана
        self.screen_height = 800 # высота экрана
        self.bg_color = (fon) # фон


        self.bullet_width = 5 # ширина снаряда
        self.bullet_height = 28  # высота снаряда
        self.bullet_color = (255, 0, 0) # цвет снаряда
        self.bullet_allowed = 100 # кол-во допустимых патрон до выхода за границу

        self.fleet_drop_speed = 15
        self.fleet_direction = 1
        self.ship_limit = 0
        self.speedup = 1.05
        self.dynamic_settings()
        self.score_scale = 1.3


    def dynamic_settings(self):
        self.ship_speed_fact = 1
        self.bullet_speed_fact = 3.5
        self.alien_speed_fact = 0.3
        self.fleet_direction = 1.0
        self.alien_spoint = 10
    def new_speed(self):
        self.alien_speed_fact *= self.speedup
        self.alien_spoint = int(self.alien_spoint * self.score_scale)
