import pygame
from random import randint
import time
import numpy as np
import pandas as pd
from DQN import Agent
from database import create_connection, create_database, create_table, insert_data 

# Assets
image_background    = 'assets/background/galaxy.jpg'  # Background
image_ship          = 'assets/sprites/space_ship_state.png'  # Player
image_bullet        = 'assets/sprites/laser.png'  # Bullets
image_alien         = 'assets/sprites/alien.png'  # Enemy
image_icon          = 'assets/background/icon.png'  # Icon
font_name           = "assets/font/Starjout.ttf"  # Font


class GameSprite(pygame.sprite.Sprite):
    """Main class for sprites"""
    def __init__(self, window, win_height, win_width, 
                 player_image, cord_x, cord_y, width, height, speed):
        pygame.sprite.Sprite.__init__(self)

        # Window
        self.window = window
        self.window_height = win_height
        self.window_width = win_width

        # Sprite object
        self.image = pygame.transform.scale(pygame.image.load(
            player_image), (width, height))  

        self.speed = speed

        # Object's hitbox
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

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
            # We're ready to fire when 300 ms have passed.
            if abs(self.current_time - self.previous_time) > 300:
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

    def collissionShip(self, ship):
        if self.rect.colliderect(ship.rect):
            return True
        
    def update(self):
        self.rect.y += self.speed

    def updateMove(self):
        if self.rect.y > self.window_height or self.collissionShip(self.ship):
            return True
    
    def collisionBullet(self):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet.rect):
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
    def __init__(self, num_games, gamma, lr):
        # Connection to database
        host = 'localhost'
        user = 'root'
        password = '0000'
        database = 'dql_data'

        create_database(host, user, password, database)
        self.connection = create_connection(host, user, password, database)
        create_table(self.connection)

        # Vars
        self.score_points = 0
        self.record_score_points = 0
        self.reward = 0
        self.n_games = num_games
        self.gamma = gamma
        self.lr = lr

        self.finish = False
        self.game = True
        
        self.previous_time = pygame.time.get_ticks()
        
        # Create a window
        self.window_width = 400
        self.window_height = 600
        pygame.display.set_caption("Space War")
        pygame.display.set_icon(pygame.image.load(image_icon))
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.transform.scale(pygame.image.load(image_background),
                                            (self.window_width, self.window_height))
        
        # Label
        pygame.font.init()
        self.font = pygame.font.Font(font_name, 25)
        self.record_score = self.font.render(f'Record: {self.record_score_points}', True, (255, 232, 31))
        self.score = self.font.render(f'Score: {self.score_points}', True, (255, 232, 31))

        # Creating star ship
        self.ship = Player(self.window, self.window_height, self.window_width,
                            image_ship, self.window_width / 2, self.window_height-50, 60, 50, 8)
        # Creating groups for objects
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Creating aliens
        self.createAliens()

        self.createAgent(self.gamma, self.lr)

        self.observation = self.getObjectsPos()
        self.observation_ = self.getObjectsPos()

        self.dataFrame = pd.DataFrame(columns=['Episode','Score', 'Record', 'Epsilon', 'Gamma', 'Alpha', 'Duration(s)'])

    def createAgent(self, gamma, lr):
        self.agent = Agent(gamma, lr, epsilon=1,  eps_end=0.05, eps_dec=5e-4, 
                              batch_size=64, n_actions=3, input_dims=[18,])

    def getObjectsPos(self):
        cordArray = np.zeros(2 * 9, dtype=np.float32)
        cordArray[0], cordArray[1] = self.ship.getPos()
        index = 2
        for alien in self.aliens:
            cordArray[index], cordArray[index+1] = alien.getPos()
            index += 2
        for bullet in self.bullets:
            cordArray[index], cordArray[index+1] = bullet.getPos()
            index += 2
        return cordArray    
    
    def createAliens(self):
        for _ in range(1, 6):
            alien = Alien(self.ship, self.bullets, self.window, self.window_height, self.window_width,
                            image_alien, randint(60, self.window_width-60), -40, 50, 50, 4)
            self.aliens.add(alien)

    def drawSprites(self):
        self.bullets.draw(self.window)
        self.aliens.draw(self.window)
        self.ship.reset()

    def blitWindow(self):
        # Update background
        self.window.blit(self.background, (0,0))  # Background
        self.window.blit(self.record_score, (10, 0))  # Record score label
        self.window.blit(self.score, (10, 25))  # Score label
            

    def addToDataFrame(self, df, episode, score, record, epsilon, gamma, alpha, duration):
        new_row = pd.DataFrame({
            'Episode': [episode],
            'Score': [score],
            'Record': [record],
            'Epsilon': [epsilon],
            'Gamma': [gamma],
            'Alpha': [alpha],
            'Duration(s)': [duration]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        return df
    
    def game_loop(self):
        startLearnTime = time.time()
        for episode in range(1, self.n_games+1):
            startEpisodeTime = time.time()
            self.game = True
            self.finish = False
            while self.game:  # Game loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                if not self.finish:        
                    self.blitWindow()
                    self.reward = 0
                    self.action = self.agent.choose_action(self.observation)
                    self.ship.update(self.action, self.bullets)
                    self.bullets.update()
                    self.aliens.update()
                    # Sprites draw
                    self.drawSprites()
                    for alien in self.aliens:
                        if alien.collisionBullet():
                            self.score_points += 1
                            self.reward += 100
                            self.score = self.font.render(f'Score: {self.score_points}',
                                                           True, (255, 232, 31))
                        elif alien.updateMove():
                            self.aliens.empty()
                            self.finish = True
                            self.reward -= 1000
                            if self.score_points > self.record_score_points:
                                self.record_score_points = self.score_points
                                self.record_score = self.font.render(f'Record: {self.record_score_points}',
                                                                    True, (255, 232, 31))
                    self.observation_ = self.getObjectsPos()
                    self.agent.store_transition(self.observation, self.action, self.reward,
                                        self.observation_, self.finish)
                    self.agent.learn()
                    self.observation = self.observation_
                else:
                    endEpisodeTime = time.time()
                    episodeDuration = endEpisodeTime - startEpisodeTime
                    self.dataFrame = self.addToDataFrame(self.dataFrame, episode, self.score_points, 
                                                            self.record_score_points, self.agent.epsilon, 
                                                            self.agent.gamma, self.agent.lr, episodeDuration)
                    insert_data(self.connection, episode, self.score_points, self.record_score_points,
                                     self.agent.epsilon, self.agent.gamma, self.agent.lr, episodeDuration)
                    self.score_points = 0
                    self.createAliens()
                    self.game=False 
                pygame.display.update()
                pygame.time.delay(40)
        endLearnTime = time.time()
        learnDuration = endLearnTime - startLearnTime

             
GamePlay = Game(500, 0.99, 0.001)
GamePlay.game_loop()