import pygame.font


class Button():
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect  = self.screen.get_rect()
        self.width, self.height = 200, 50

        self.text_color = (255, 0, 0)
        self.font = pygame.font.Font('start.ttf', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)


    def prep_msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centery = self.rect.centery
        self.msg_image_rect.centerx = self.rect.centerx -15


    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
