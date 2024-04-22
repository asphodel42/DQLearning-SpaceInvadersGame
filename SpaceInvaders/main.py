import pygame
import time
import emoji
from random import randint


# Assets
image_background    = 'SpaceInvaders/assets/background/galaxy.jpg'  # Background
image_ship          = 'SpaceInvaders/assets/sprites/space_ship_state.png'  # Player
image_bullet        = 'SpaceInvaders/assets/sprites/laser.png'  # Bullets
image_alien         = 'SpaceInvaders/assets/sprites/alien.png'  # Enemy
sound_music         = 'SpaceInvaders/assets/music/space.ogg'  # Music
sound_shoot         = 'SpaceInvaders/assets/music/shoot_sound.ogg'
sound_explosion     = 'SpaceInvaders/assets/music/explosion.ogg'  # Explosion
image_icon          = 'SpaceInvaders/assets/background/icon.png'  # Icon
font_name           = "SpaceInvaders/assets/font/Starjout.ttf"  # Font

class GameSprite(pygame.sprite.Sprite):
    """Main class for sprites"""
    def __init__(self, window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed):  # Initialization
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.window_height = win_height
        self.window_width = win_width

        self.image = pygame.transform.scale(pygame.image.load(
            player_image), (width, height))  # Sprite object

        self.speed = speed  # Speed

        # Object's hitbox
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # Draw a sprite 
    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(GameSprite):
    # controls
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < self.window_width - 105:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > 600:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < self.window_height - 105:
            self.rect.y += self.speed


    # Create a bullet that's moving up
    def fire(self):
        bullet = Bullet(self.window, self.window_height, self.window_width,
                         image_bullet, self.rect.centerx, self.rect.y, 10, 60, 20)
        return bullet
    


class Alien(GameSprite):
    def __init__(self, ship, bullets, window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed):
        super().__init__(window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed)
        self.ship = ship
        self.bullets = bullets

    def updateMove(self, missed_aliens):
        self.rect.y += self.speed
        # Disapear if crossed the edge of window
        if self.rect.y > self.window_height:
            self.rect.x = randint(100, self.window_width - 100)
            self.rect.y = 0
            missed_aliens += 1
        return missed_aliens

    def collissionShip(self, ship, current_lives):
        if self.rect.colliderect(ship.rect):
            current_lives -= 1
            print(current_lives)
            self.rect.x = randint(80, self.window_width-80)
            self.rect.y = -40
        return current_lives

    def collisionBullet(self, score_points):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet.rect):
                # explosion_sound.play()
                bullet.kill()
                self.rect.x = randint(80, self.window_width-80)
                self.rect.y = -40
                score_points += 1
        return score_points


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -100:
            self.kill()
        
class Game():
    def __init__(self):
        # Vars
        self.score_points = 0
        self.missed_aliens = 0
        self.current_lives = 3  # Number of HP

        self.finish = False
        self.game = True

        # Create a window
        self.window_width = 1300
        self.window_height = 800
        pygame.display.set_caption("Space War")
        pygame.display.set_icon(pygame.image.load(image_icon))
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Creating background
        self.background = pygame.transform.scale(pygame.image.load(image_background),
                                            (self.window_width, self.window_height))

        # Creating star ship
        self.ship = Player(self.window, self.window_height, self.window_width,
                            image_ship, 5, self.window_height-100, 120, 100, 15)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Creating aliens
        for _ in range(1, 6):
            alien = Alien(self.ship, self.bullets, self.window, self.window_height, self.window_width,
                           image_alien, randint(100, self.window_width-100), -40, 100, 100, randint(1, 4))
            self.aliens.add(alien)

        # # Music
        # pygame.mixer.init()
        # pygame.mixer.music.load(sound_music)
        # pygame.mixer.music.set_volume(0.05)
        # pygame.mixer.music.play()
        # shoot_sound = pygame.mixer.Sound(sound_shoot)
        # shoot_sound.set_volume(0.1)
        # explosion_sound = pygame.mixer.Sound(sound_explosion)
        # explosion_sound.set_volume(0.1)

        # Label
        pygame.font.init()
        self.font = pygame.font.Font(font_name, 25)
        # self.font_finish = pygame.font.Font(None, 100)
        # self.lost = self.font_finish.render('YOU LOST', True, (120, 13, 31))
        # self.win = self.font_finish.render('YOU WIN', True, (32, 252, 3))

    def game_loop(self):
        while self.game:  # Game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bullets.add(self.ship.fire())
                    # shoot_sound.play()

            
            if not self.finish:
                # Render fonts
                self.score = self.font.render(f'Score: {self.score_points}', True, (255, 232, 31))
                self.missed = self.font.render(f'Missed: {self.missed_aliens}', True, (255, 232, 31))
                self.hp = self.font.render(f'{self.current_lives}', True, (255, 232, 31))
                
                # Update background
                self.window.blit(self.background, (0,0))  # Background
                self.window.blit(self.score, (10, 0))  # Score label
                self.window.blit(self.missed, (10, 25))  # Missed label
                self.window.blit(self.hp, (self.window_width - 50, 15))  # HP Label

                # Update movement
                for alien in self.aliens:
                    self.score_points = alien.collisionBullet(self.score_points)
                    self.current_lives = alien.collissionShip(self.ship, self.current_lives)
                    self.missed_aliens = alien.updateMove(self.missed_aliens)

                self.bullets.update()
                self.aliens.update()
                self.ship.update()

                # Sprites draw
                self.bullets.draw(self.window)
                self.aliens.draw(self.window)
                self.ship.reset()

                # Losing
                if self.current_lives <= 0:
                    self.finish = True
                #     window.blit(lost, (window_width/2 - 200, window_height/2 - 50))
                if self.missed_aliens >= 6:
                    self.finish = True
                #     window.blit(lost, (window_width/2 - 200, window_height/2 - 50))

                # Winning
                if self.score_points >= 30:
                    self.finish = True
                    # window.blit(win, (500, 400))
            else:
                self.current_lives = 3
                self.missed_aliens = 0
                self.score_points = 0
                self.finish = False
            pygame.display.update()

            pygame.time.delay(30)
            
            
        

GamePlay = Game()
GamePlay.game_loop()