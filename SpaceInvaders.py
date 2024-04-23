import pygame
from random import randint
from DQN import Agent


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
        # if keys[pygame.K_w] and self.rect.y > 600:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_s] and self.rect.y < self.window_height - 105:
        #     self.rect.y += self.speed


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
        self.pos_x = 0
        self.pos_y = 0
        
    def updateMove(self):
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y
        self.rect.y += self.speed
        # Disapear if crossed the edge of window
        if self.rect.y > self.window_height:
            return True
        else: return False

    def getPos(self):
        return [self.pos_x, self.pos_y]
    def collissionShip(self, ship):
        if self.rect.colliderect(ship.rect):
            return True

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
        # self.missed_aliens = 0
        # self.current_lives = 3  # Number of HP

        self.finish = False
        self.game = True
        self.record_score_points = 0
        self.previous_time = pygame.time.get_ticks()

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
        self.createAliens()

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
    
    def onScreenUpdate(self):
        self.surface_array = pygame.surfarray.array3d(pygame.display.get_surface())  

    def createAliens(self):
        for _ in range(1, 6):
            alien = Alien(self.ship, self.bullets, self.window, self.window_height, self.window_width,
                            image_alien, randint(100, self.window_width-100), -40, 100, 100, randint(1, 4))
            self.aliens.add(alien)

    def alienCollision(self):
        for alien in self.aliens:
            if alien.collissionShip(self.ship) or alien.updateMove():
                # self.current_lives -= 1
                self.aliens.empty()
                return True

    def game_loop(self):
        while self.game:  # Game loop
            agent = Agent(gamma=0.99, epsilon=1, eps_end=0.001, eps_dec=1e-4, lr=0.001, 
                              batch_size=64, n_actions=3, input_dims=[8])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.current_time = pygame.time.get_ticks()
                    # We're ready to fire when 500 ms have passed.
                    if self.current_time - self.previous_time > 200:
                        self.previous_time = self.current_time
                        self.bullets.add(self.ship.fire())
                    # shoot_sound.play()
            
            if not self.finish:
                self.aliensCord = []

                # Render fonts
                self.record_score = self.font.render(f'Record: {self.record_score_points}', True, (255, 232, 31))
                self.score = self.font.render(f'Score: {self.score_points}', True, (255, 232, 31))
                
                # Update background
                self.window.blit(self.background, (0,0))  # Background
                self.window.blit(self.record_score, (10, 0))  # Record score label
                self.window.blit(self.score, (10, 25))  # Score label
                
                self.bullets.update()
                self.aliens.update()
                self.ship.update()

                # Sprites draw
                self.bullets.draw(self.window)
                self.aliens.draw(self.window)
                self.ship.reset()

                # Update movement
                for alien in self.aliens:
                    self.score_points = alien.collisionBullet(self.score_points)
                    self.aliensCord.append(alien.getPos()) 

                # print(f"ALines has cords: {self.aliensCord}")
                # Losing
                if self.alienCollision():
                    self.finish = True
                    if self.score_points > self.record_score_points:
                        self.record_score_points = self.score_points
            else:
                self.score_points = 0
                self.createAliens()
                self.finish = False

            pygame.display.update()
            self.onScreenUpdate()
            pygame.time.delay(10)
            
            
    
GamePlay = Game()
GamePlay.game_loop()