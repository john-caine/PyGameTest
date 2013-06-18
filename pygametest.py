import sys
import pygame 

from constants import *

import game


import title_screen

if __name__ == "__main__":
  pygame.init()
  pygame.key.set_repeat(100, 100)
    
  columns = rows = 20
  size = width, height = tile_size[0] * columns,  tile_size[1] * rows
  screen = pygame.display.set_mode(size)

  title_screen.run(screen)
  
  game.play(screen)
