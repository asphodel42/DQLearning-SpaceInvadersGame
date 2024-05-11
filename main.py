import pygame
from random import randint
import time
import numpy as np
import pandas as pd
from DQN import Agent
from database import create_connection, create_database, create_table, insert_data, addToDataFrame, createPlot
from SpaceInvaders import Player, Alien

image_icon          = 'assets/background/icon.png'  # Icon
image_background    = 'assets/background/galaxy.jpg'  # Background
image_ship          = 'assets/sprites/space_ship_state.png'  # Player
font_name           = "assets/font/Starjout.ttf"  # Font
image_alien         = 'assets/sprites/alien.png'  # Enemy
image_bullet        = 'assets/sprites/laser.png'  # Bullets
  
class Game():
    def __init__(self, num_games, gamma, lr, tablename, filename):
        # Connection to database
        host = 'localhost'
        user = 'root'
        password = '0000'
        database = 'dql_data'
        self.tablename = tablename
        self.filename = filename

        create_database(host, user, password, database)
        self.connection = create_connection(host, user, password, database)
        create_table(self.connection, self.tablename)

        # Vars
        self.score_points = 0
        self.mean = 0
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
                            image_ship, image_bullet, self.window_width / 2, self.window_height-50, 60, 50, 5)
        # Creating groups for objects
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Creating aliens
        self.createAliens()

        self.createAgent(self.gamma, self.lr)

        self.observation = self.getObjectsPos()
        self.new_observation = self.getObjectsPos()

        self.dataFrame = pd.DataFrame(columns=['Episode','Score', 'Mean', 'Record', 
                                               'Epsilon', 'Gamma', 'Alpha', 'Duration(s)'])

    def createAgent(self, gamma, lr):
        self.agent = Agent(gamma, lr, epsilon=1,  eps_end=0.05, eps_dec=5e-4, 
                              batch_size=64, n_actions=3, input_dims=[52,])
  
    def getObjectsPos(self):
        cordArray = np.zeros(2 * 26, dtype=np.float32)
        cordArray[0], cordArray[1], cordArray[2], cordArray[3] = self.ship.getPos()
        index = 4
        for alien in self.aliens:
            cordArray[index], cordArray[index+1], cordArray[index+2], cordArray[index+3] = alien.getPos()
            index += 4
        for bullet in self.bullets:
            cordArray[index], cordArray[index+1], cordArray[index+2], cordArray[index+3] = bullet.getPos()
            index += 4
        return cordArray 
    
    def createAliens(self):
        for _ in range(1, 6):
            alien = Alien(self.bullets, self.window, self.window_height, self.window_width,
                            image_alien, randint(60, self.window_width-60), -40, 50, 50, randint(3, 6))
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
    
    def game_loop(self):
        startLearnTime = time.time()
        for episode in range(1, self.n_games+1):
            startEpisodeTime = time.time()
            self.game = True
            self.finish = False
            while self.game:  # Game loop
                self.score = self.font.render(f'Score: {self.score_points}',
                                                           True, (255, 232, 31))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                self.reward = 0
                if not self.finish:        
                    self.blitWindow() 
                    self.action = self.agent.choose_action(self.observation)
                    self.ship.update(self.action, self.bullets)
                    self.bullets.update()
                    self.aliens.update()
                    # Sprites draw
                    self.drawSprites()
                    # if self.action == 0 or self.action == 1:
                    #     self.reward -= 1
                    for alien in self.aliens:
                        if alien.rect.y >= self.window_height:
                            alien.rect.y = - 20
                            alien.rect.x = randint(50, self.window_width-50)
                        elif alien.collisionBullet():
                            self.score_points += 1
                            self.reward += 100
                            self.score = self.font.render(f'Score: {self.score_points}',
                                                           True, (255, 232, 31))
                        elif alien.collissionShip(self.ship):
                            self.aliens.empty()
                            self.finish = True
                            self.reward -= 200
                            if self.score_points > self.record_score_points:
                                self.record_score_points = self.score_points
                                self.record_score = self.font.render(f'Record: {self.record_score_points}',
                                                                    True, (255, 232, 31))
                    self.new_observation = self.getObjectsPos()
                    self.agent.store_transition(self.observation, self.action, self.reward,
                                        self.new_observation, self.finish)
                    self.agent.learn()
                    self.observation = self.new_observation
                else:
                    endEpisodeTime = time.time()
                    episodeDuration = endEpisodeTime - startEpisodeTime
                    self.dataFrame = addToDataFrame(self.dataFrame, episode, self.score_points, 
                                                            self.record_score_points, self.agent.epsilon, 
                                                            self.agent.gamma, self.agent.lr, episodeDuration)
                    self.mean = self.dataFrame.at[episode-1, "Mean"]
                    insert_data(self.connection, self.tablename, episode, self.score_points, self.mean,
                                self.record_score_points, self.agent.epsilon, self.agent.gamma, 
                                self.agent.lr, episodeDuration)
                    createPlot(self.dataFrame["Episode"].to_list(), self.dataFrame["Score"].to_list(),
                                self.dataFrame["Mean"].to_list(), self.filename)
                    self.score_points = 0
                    self.createAliens()
                    self.game=False 
                pygame.display.update()
                pygame.time.delay(5)
        endLearnTime = time.time()
        learnDuration = endLearnTime - startLearnTime

if __name__ == "__main__":      
    GamePlay = Game(5000, 0.6, 0.0001, 'game_dat_06_00001', 'statistics/graphs/DQLearning06_00001.jpg')
    GamePlay.game_loop()