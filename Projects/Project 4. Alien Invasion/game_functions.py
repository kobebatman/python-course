import sys
import pygame
from settings import Settings

def check_events():
  ''' Event шалгах '''

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

def update_screen(screen, ship):
  ''' Дэлгэц шинэчлэн зурах '''

  screen.fill(Settings.background_color)
  ship.draw()
  pygame.display.flip()