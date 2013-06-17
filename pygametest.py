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
    self.background_position = { 'x': x, 'y': y }

  def set_rect(self):
    self.rect = self.image.get_rect().move(
      tile_size[0] * self.background_position['x'],
      tile_size[1] * self.background_position['y'])

class Tile(GameObject):
  def __init__(self, background, x, y, image_name):
    super(Tile, self).__init__(x, y)
    self.image = pygame.image.load(image_name).convert()
    self.set_rect()
    self.background = background
    self.background.tiles.add(self)

class GrassTile(Tile):
  def __init__(self, background, x, y):
    self._image_name = "grass.jpg"
    super(GrassTile, self).__init__(background, x, y, self._image_name)

class RockTile(Tile):
  def __init__(self, background, x, y):
    self._image_name = "rock.jpg"
    super(RockTile, self).__init__(background, x, y, self._image_name)
    self.background.collidable.add(self)

class WaterTile(Tile):
  def __init__(self, background, x, y):
    self._image_name = "water.jpg"
    super(WaterTile, self).__init__(background, x, y, self._image_name)
    self.background.collidable.add(self)

class Background:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.tiles = pygame.sprite.Group()
    self.collidable = pygame.sprite.Group()

    y = 0
    for line in open('background.txt'):
      x = 0
      for character in line:
        self.rows += 1
        if character == 'w':
          WaterTile(self, x, y)
        elif character == 'g':
          GrassTile(self, x, y)
        elif character == 'r':
          RockTile(self, x, y)
        else:
          break
        x += 1
      y += 1

  def draw(self, surface):
    self.tiles.draw(surface)

class Player(GameObject):
  def __init__(self, background, x, y):
    super(Player, self).__init__(x, y)
    self.image = pygame.image.load('player.png').convert()
    self.set_rect()
    self.background = background

  def move(self, x, y):
    old_x = self.background_position['x']
    old_y = self.background_position['y']
    self.background_position['x'] = x
    self.background_position['y'] = y
    self.set_rect()

    collisions = pygame.sprite.spritecollide(self, self.background.collidable, False)
    if len(collisions) > 0:
      self.background_position['x'] = old_x
      self.background_position['y'] = old_y
      self.set_rect()


  def down(self):
    self.move(self.background_position['x'], self.background_position['y'] + 1)

  def up(self):
    self.move(self.background_position['x'], self.background_position['y'] - 1)

  def left(self):
    self.move(self.background_position['x'] - 1, self.background_position['y'])

  def right(self):
    self.move(self.background_position['x'] + 1, self.background_position['y'])

tile_size = (32,32)

if __name__ == "__main__":
  pygame.init()

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

    background.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
