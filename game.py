import sys
import pygame 

from constants import *

import background
import player

def play(screen):
  level_background = background.Background()
  level_player = player.Player(level_background, 0, 0)
  player_group = pygame.sprite.Group()
  player_group.add(level_player)

  while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          level_player.down()
        elif event.key == pygame.K_UP:
          level_player.up()
        elif event.key == pygame.K_LEFT:
          level_player.left()
        elif event.key == pygame.K_RIGHT:
          level_player.right()
        if event.key == pygame.K_ESCAPE:
          sys.exit()
          
    level_background.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()