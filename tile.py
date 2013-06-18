from game_object import *

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
    self.background.walkable.add(self)

class RockTile(Tile):
  def __init__(self, background, x, y):
    self._image_name = "rock.jpg"
    super(RockTile, self).__init__(background, x, y, self._image_name)

class WaterTile(Tile):
  def __init__(self, background, x, y):
    self._image_name = "water.jpg"
    super(WaterTile, self).__init__(background, x, y, self._image_name)
