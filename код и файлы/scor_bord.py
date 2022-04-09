import pygame.font
from pygame.sprite import Group
from ship import Ship


class score_board():
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.screen
        self.stats = ai_game.stats
        self.text_color = (255, 0, 0)
        self.font = pygame.font.Font('scor.otf', 45)
        self.prep_high_score()
        self.prep_scor()
        self.preep_lvl()
        self.preep_ship()



    def prep_scor(self):
        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 35
        self.score1_image = self.font.render("Score", True, self.text_color)
        self.score1_rect = self.score1_image.get_rect()
        self.score1_rect.right = self.screen_rect.right - 10
        self.score1_rect.top = 0


    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = self.screen_rect.midtop
        self.high_score_rect.top = 35
        self.score2_image = self.font.render("High Score", True, self.text_color)
        self.score2_rect = self.score2_image.get_rect()
        self.score2_rect.centerx = self.screen_rect.centerx
        self.score2_rect.centery = self.screen_rect.centery
        self.score2_rect.top = 0


    def check_high_score(self):
        if self.stats.score > self.stats.high_score :
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def preep_lvl(self):
        lvl_str = str(self.stats.lvl)
        self.lvl_image = self.font.render(lvl_str, True, self.text_color)
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.left = self.screen_rect.left + 20
        self.lvl_rect.top = 35
        self.lvl1_image = self.font.render("level", True, self.text_color)
        self.lvl1_rect = self.lvl1_image.get_rect()
        self.lvl1_rect.left = self.screen_rect.left
        self.lvl1_rect.top = 0

    def preep_ship(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)






    def show_scor(self):
        self.screen.blit(self.lvl1_image, self.lvl1_rect)
        self.screen.blit(self.score2_image, self.score2_rect)
        self.screen.blit(self.score1_image, self.score1_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)
