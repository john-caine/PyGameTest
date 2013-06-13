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

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super(GameObject, self).__init__()
    self.map = { 'x': x, 'y': y }

  def set_rect(self):
    self.rect = self.image.get_rect().move(
      tile_size[0] * self.map['x'],
      tile_size[1] * self.map['y'])

class Tile(GameObject):
  def __init__(self, image_name, x, y):
    super(Tile, self).__init__(x, y)
    self.image = pygame.image.load(image_name).convert()
    self.set_rect()

class Map:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.tiles = pygame.sprite.Group()
    for x in range(0, self.columns):
      for y in range(0, self.rows):
        self.tiles.add(Tile(random.choice(['grass.jpg', 'rock.jpg', 'water.jpg']) , x, y))

  def draw(self, surface):
    self.tiles.draw(surface)

class Player(GameObject):
  def __init__(self, x, y):
    super(Player, self).__init__(x, y)
    self.image = pygame.image.load('player.png').convert()
    self.set_rect()
      
  def down(self):
    self.map['y'] += 1
    self.set_rect()

  def up(self):
    self.map['y'] -= 1
    self.set_rect()
    
  def left(self):
    self.map['x'] -= 1
    self.set_rect()

  def right(self):
    self.map['x'] += 1
    self.set_rect()
  
tile_size = (32,32)
      
if __name__ == "__main__":
  pygame.init()

  columns = rows = 20
  size = width, height = tile_size[0] * columns,  tile_size[1] * rows
  screen = pygame.display.set_mode(size)
  
  map = Map(columns, rows)
  player = Player(0, 0)
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
    
    map.draw(screen)
    player_group.draw(screen)
    
    pygame.display.flip()
