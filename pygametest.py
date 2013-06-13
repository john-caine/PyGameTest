import sys
import pygame
import time
import math
import random

class TiledSurface(pygame.Surface):
  def __init__(self, (width, height), image_name):
    super(TiledSurface, self).__init__((width, height))
    
    image = pygame.image.load(image_name).convert()
    
    image_height = image.get_height()
    image_width = image.get_width()
    
    columns = int(math.ceil(float(height) / float(image_height)))
    rows = int(math.ceil(float(width) / float(image_width)))

    for x in range(0, columns):
      for y in range(0,rows ):
        self.blit(image, (x * image_width, y * image_height))

tile_size = (32,32)

class Tile(pygame.Surface):
  def __init__(self, image_name, x, y):
    super(Tile, self).__init__(tile_size)
    image = pygame.image.load(image_name).convert()
    self.blit(image, (0, 0))
    self.x = x
    self.y = y
    
  def draw(self, surface):
    surface.blit(self, (self.x * tile_size[0], self.y * tile_size[1]))

class Map:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.tiles = []
    for x in range(0, self.columns):
      for y in range(0, self.rows):
        self.tiles.append(Tile(random.choice(['grass.jpg', 'rock.jpg', 'water.jpg']) , x, y))

  def draw(self, surface):
    for tile in self.tiles:
      tile.draw(surface)

if __name__ == "__main__":
  pygame.init()

  columns = rows = 20
  size = width, height = tile_size[0] * columns,  tile_size[1] * rows
  screen = pygame.display.set_mode(size)
  
  map = Map(columns, rows)

  while True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
    
    map.draw(screen)
    
    pygame.display.flip()
