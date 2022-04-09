import sys
import pygame
from  time import sleep

from settings import set
from ship import Ship
from bullet import Bullet
from alien import  Alien
from game_stat import Game_stat
from button import Button
from scor_bord import score_board

class AlienInvassion:
    def __init__(self): # создает ресурсы инициализирует игру
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init() # настройки для норм работы пучгейма
        self.settings = set() # перенос настроек
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.mixer.music.load('shot.mp3')
        self.shot = pygame.mixer.Sound('shot.mp3')
        self.shot.set_volume(0.02)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # настройки окна
        pygame.display.set_caption("Инопришеленцы наступают") # название окна
        self.stats = Game_stat(self)
        self.sb = score_board(self)
        self.ship = Ship(self)
        self.play_button = Button(self, "Start")
        self.screen.blit(self.settings.bg_color, (0, 0)) # настройки фона
        self.bullets = pygame.sprite.Group()# группа для прорисовки снарядов
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.fon_muz = pygame.mixer.music.load('razee.mp3')
        self.fon_muz = pygame.mixer.Sound('razee.mp3')
        self.fon_muz.set_volume(0.04)
        self.fon_muz.play(-1)





    def run_game(self): # основной цикл игры
        while True:
            self._check_events()  # для вызова в функции
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()  # обновление инфы о пулях
                self._update_aliens()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self._update_screen()  # обновление экрана



    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.сheck_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        

    def _check_events(self): # набор всякого
        for event in pygame.event.get(): # отслеживания событий клавиатуры и мыши
            if event.type == pygame.QUIT: #выход
                sys.exit() # выход
            elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event) # если кнопка нажата обратиться в ф-ию
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event) # если кнопка нажата и отпущена обратиться в ф-ию
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def _check_keydown_events(self, event): # функция если кнопка нажата
        if self.stats.game_active == True:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event): #функция если кнопка нажата и отпущена
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_play_button(self, mouse_pos):
        button_click = self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.stats.game_active:
            self.settings.dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_scor()
            self.sb.preep_lvl()
            self.sb.preep_ship()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)




    def _fire_bullet(self):
        if (len(self.bullets) < self.settings.bullet_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shot.play()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_heidght = alien.rect.size
        alien_width =alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * alien_heidght) - ship_height)
        number_rows = available_space_y // (5 * alien_heidght)
        for row_number in range(number_rows):
            for alien_number in range(numbers_aliens_x):
                self._create_alien(alien_number, row_number)


    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.hit_ship()
                break


    def _create_alien (self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x  = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y =  alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany (self.ship, self.aliens):
            self.hit_ship()
        self.check_aliens_bottom()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            self.check_bullet_alien_coll()

    def check_bullet_alien_coll(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.settings.new_speed()
            self.bullets.empty()
            self._create_fleet()
            self.stats.lvl +=1
            self.sb.preep_lvl()
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_spoint * len(aliens)
            self.sb.prep_scor()
            self.sb.check_high_score()

    def hit_ship(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -=1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)




    def _update_screen(self): # функция прорисовки всего
        self.screen.blit(self.settings.bg_color, (0, 0)) # прорисовка корабля
        self.ship.blitme() # рисуется корабль
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() # прорисовка пуль
        self.bullets.update()# обновление инфы о пулях
        self.aliens.draw(self.screen)
        self.sb.show_scor()
        if not self.stats.game_active:
            self.play_button.draw()

        pygame.display.flip()  # обновление экрана






if __name__ == '__main__':
    ai = AlienInvassion() # создание экземпляра
    ai.run_game() # запуск игры