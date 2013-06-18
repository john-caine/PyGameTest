import pygame

from constants import *

from tile import *

class Background:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.tiles = pygame.sprite.Group()
    self.walkable = pygame.sprite.Group()

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
