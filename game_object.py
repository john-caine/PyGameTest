import pygame

from constants import *

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super(GameObject, self).__init__()
    self.background_position = { 'x': x, 'y': y }

  def set_rect(self):
    self.rect = self.image.get_rect().move(
      tile_size[0] * self.background_position['x'],
      tile_size[1] * self.background_position['y'])
