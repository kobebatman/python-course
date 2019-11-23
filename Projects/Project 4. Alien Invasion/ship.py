import pygame

class Ship:
  ''' Байлдааны хөлөг '''

  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    
    # Шинэ хөлгийг дэлгэцийн голд байрлуулах
    self.rect.centerx = self.screen_rect.centerx

    # Шинэ хөлгийг дэлгэцийн доор байрлуулах
    self.rect.bottom = self.screen_rect.bottom

  def draw(self):
    ''' rect-ийн байрлалд ship-ийн image зурах '''
    self.screen.blit(self.image, self.rect)