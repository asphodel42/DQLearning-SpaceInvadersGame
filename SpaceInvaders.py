import pygame
from random import randint

# Assets
class GameSprite(pygame.sprite.Sprite):
    """Main class for sprites"""
    def __init__(self, window, win_height, win_width, 
                 player_image, cord_x, cord_y, width, height, speed):
        pygame.sprite.Sprite.__init__(self)

        # Window
        self.window = window
        self.window_height = win_height
        self.window_width = win_width

        self.width = width
        self.height = height

        # Sprite object
        self.image = pygame.transform.scale(pygame.image.load(
            player_image), (width, height))  

        self.speed = speed

        # Object's hitbox
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y

    def getPos(self):
        return [self.rect.left, self.rect.left+self.width, self.rect.top, self.rect.top+self.height]

    # Draw a sprite 
    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(GameSprite):
    def __init__(self, window, win_height, win_width, 
                 player_image, image_bullet, player_x, player_y, width, height, speed):
        super().__init__(window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed)
        self.current_time = pygame.time.get_ticks()
        self.previous_time = self.current_time
        self.image_bullet = image_bullet
    # controls
    def update(self, action, bullets):
        # keys = pygame.key.get_pressed()
        if action == 0 and self.rect.x > 5:
            self.rect.x -= self.speed
        if action == 1 and self.rect.x < self.window_width - 60:
            self.rect.x += self.speed
        if action == 2:
            self.current_time = pygame.time.get_ticks()
            # We're ready to fire when 300 ms have passed.
            if abs(self.current_time - self.previous_time) > 100:
                bullets.add(self.fire())
                self.previous_time = self.current_time 
               
    # Create a bullet that's moving up
    def fire(self):
        bullet = Bullet(self.window, self.window_height, self.window_width,
                         self.image_bullet, self.rect.centerx, self.rect.y, 10, 60, 100)
        return bullet
    

class Alien(GameSprite):
    def __init__(self, bullets, window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed):
        super().__init__(window, win_height, win_width, 
                 player_image, player_x, player_y, width, height, speed)
        self.bullets = bullets
        self.pos_x = 0
        self.pos_y = 0

    def collissionShip(self, ship):
        if self.rect.colliderect(ship.rect):
            return True
        
    def update(self):
        self.rect.y += self.speed
    
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