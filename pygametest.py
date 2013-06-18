import sys
import pygame

from constants import *

from background import *
from player import *

if __name__ == "__main__":
  pygame.init()
  pygame.key.set_repeat(100, 100)
  
  columns = rows = 20
  size = width, height = tile_size[0] * columns,  tile_size[1] * rows
  screen = pygame.display.set_mode(size)

  background = Background(columns, rows)
  player = Player(background, 0, 0)
  player_group = pygame.sprite.Group()
  player_group.add(player)

  while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          player.down()
        elif event.key == pygame.K_UP:
          player.up()
        elif event.key == pygame.K_LEFT:
          player.left()
        elif event.key == pygame.K_RIGHT:
          player.right()
        elif event.key == pygame.K_ESCAPE:
          sys.exit()

    background.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
