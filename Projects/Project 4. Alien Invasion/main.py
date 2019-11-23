import sys
import pygame
import game_functions
from settings import Settings
from ship import Ship

def start_game():
  ''' Тоглоом эхлүүлэх '''

  pygame.init()
  screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
  pygame.display.set_caption(Settings.game_caption)

  # Шинэ хөлөг үүсгэх
  ship = Ship(screen)

  while True:
    # Event шалгах
    game_functions.check_events()

    # Дэлгэц шинэчлэн зурах
    game_functions.update_screen(screen, ship)

start_game()