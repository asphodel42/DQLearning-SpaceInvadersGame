import pygame
from random import randint
from DQN import Agent
import numpy as np


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

    def getPos(self):
        return [self.rect.centerx, self.rect.centery]

    # Draw a sprite 
    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(GameSprite):
    def __init__(self, window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed):
        super().__init__(window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed)
        self.current_time = pygame.time.get_ticks()
        self.previous_time = self.current_time
    # controls
    def update(self, action, bullets):
        # keys = pygame.key.get_pressed()
        if action == 0 and self.rect.x > 5:
            self.rect.x -= self.speed
        if action == 1 and self.rect.x < self.window_width - 105:
            self.rect.x += self.speed
        if action == 2:
            self.current_time = pygame.time.get_ticks()
            # We're ready to fire when 500 ms have passed.
            if self.current_time - self.previous_time > 500:
                bullets.add(self.fire())
                self.previous_time = self.current_time 
               
    # Create a bullet that's moving up
    def fire(self):
        bullet = Bullet(self.window, self.window_height, self.window_width,
                         image_bullet, self.rect.centerx, self.rect.y, 10, 60, 100)
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
        self.rect.y += self.speed
        # Disapear if crossed the edge of window
        if self.rect.y > self.window_height:
            return True
        else: return False
    
    def collissionShip(self, ship):
        if self.rect.colliderect(ship.rect):
            return True

    def collisionBullet(self):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet.rect):
                # explosion_sound.play()
                bullet.kill()
                self.rect.x = randint(80, self.window_width-80)
                self.rect.y = -40
                return True 


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -100:
            self.kill()
        
class Game():
    def __init__(self):
        # Vars
        self.score_points = 0
        self.reward = 0

        self.finish = False
        self.game = True
        self.record_score_points = 0
        self.previous_time = pygame.time.get_ticks()
        
        # Create a window
        self.window_width = 400
        self.window_height = 600
        pygame.display.set_caption("Space War")
        pygame.display.set_icon(pygame.image.load(image_icon))
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Creating background
        self.background = pygame.transform.scale(pygame.image.load(image_background),
                                            (self.window_width, self.window_height))
        
        # Label
        pygame.font.init()
        self.font = pygame.font.Font(font_name, 25)

        # Creating star ship
        self.ship = Player(self.window, self.window_height, self.window_width,
                            image_ship, self.window_width / 2, self.window_height-50, 60, 50, 8)
        # Creating groups for objects
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Creating aliens
        self.createAliens()

        # TODO: get observation of a display
        self.observation = self.getObjectsPos()
        self.observation_ = self.getObjectsPos()
        


    # TODO: one of a variant of screen capturing    
    # def get_state(self):
    #     pygame.pixelcopy.surface_to_array(self.current_buffer, self.screen)
    #     print(self.current_buffer)
    #     return self.current_buffer

    def getObjectsPos(self):
        cordArray = np.zeros(2 * 8, dtype=np.float32)
        cordArray[0], cordArray[1] = self.ship.getPos()
        index = 2
        for alien in self.aliens:
            cordArray[index], cordArray[index+1] = alien.getPos()
            index += 2
        for bullet in self.bullets:
            cordArray[index], cordArray[index+1] = bullet.getPos()
        return cordArray    
    
    def onScreenUpdate(self):
        return pygame.surfarray.array2d(pygame.display.get_surface())
    
    def createAliens(self):
        for _ in range(1, 6):
            alien = Alien(self.ship, self.bullets, self.window, self.window_height, self.window_width,
                            image_alien, randint(100, self.window_width-100), -40, 50, 50, randint(2, 4))
            self.aliens.add(alien)

    def alienCollision(self):
        for alien in self.aliens:
            if alien.collissionShip(self.ship) or alien.updateMove():
                self.aliens.empty()
                return True

    def game_loop(self):
        #TODO: Create agent
        agent = Agent(gamma=0.99, epsilon=1, eps_end=0.05, eps_dec=5e-4, lr=0.001, 
                              batch_size=64, n_actions=3, input_dims=[16,])
        self.n_games = 500
        self.episode = 1
        self.scores, self.eps_history = [], []
        for episode in range(1, self.n_games):
            self.game = True
            self.finish = False
            while self.game:  # Game loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                if not self.finish:
                    # self.aliensCord = []
                    self.getObjectsPos()
                    self.reward = 0
                    #TODO: Action created by an agent
                    self.action = agent.choose_action(self.observation)


                    # Render fonts
                    self.record_score = self.font.render(f'Record: {self.record_score_points}', True, (255, 232, 31))
                    self.score = self.font.render(f'Score: {self.score_points}', True, (255, 232, 31))
                    
                    # Update background
                    self.window.blit(self.background, (0,0))  # Background
                    self.window.blit(self.record_score, (10, 0))  # Record score label
                    self.window.blit(self.score, (10, 25))  # Score label
                    
                    self.ship.update(self.action, self.bullets)
                    self.ship.update(self.action, self.bullets)
                    self.ship.update(self.action, self.bullets)
                    self.bullets.update()
                    self.aliens.update()

                    # Sprites draw
                    self.bullets.draw(self.window)
                    self.aliens.draw(self.window)
                    self.ship.reset()

                    # Update movement
                    for alien in self.aliens:
                        if alien.collisionBullet():
                            self.score_points += 1
                            self.reward += 10

                    # Losing
                    if self.alienCollision():
                        self.finish = True
                        self.reward -= 10
                        if self.score_points > self.record_score_points:
                            self.record_score_points = self.score_points
                            

                    self.observation_ = self.getObjectsPos()
                    # print("---------------------------")
                    # print(f"reward: {self.reward}")
                    # print(f"action: {self.action}")
                    # print(f"observation: {self.observation}")
                    # print(f"observation_: {self.observation_}")
                    # print(f"finish: {self.finish}")
                    agent.store_transition(self.observation, self.action, self.reward,
                                        self.observation_, self.finish)
                    agent.learn()
                    self.observation = self.observation_
                else:
                    self.scores.append(self.score_points)
                    self.eps_history.append(agent.epsilon)

                    print("Episode", episode, " | Score ", self.score_points, " | Epsilon %.2f " % agent.epsilon, " | Record ", self.record_score_points)
                    self.score_points = 0
                    self.createAliens()
                    self.game=False 
                pygame.display.update()
                pygame.time.delay(40)
             
GamePlay = Game()
GamePlay.game_loop()