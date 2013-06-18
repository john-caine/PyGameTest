from game_object import *

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

    #collisions = pygame.sprite.spritecollide(self, self.background.collidable, False)
    walkable = pygame.sprite.spritecollide(self, self.background.walkable, False)
    # if len(collisions) > 0:
      # self.background_position['x'] = old_x
      # self.background_position['y'] = old_y
      # self.set_rect()
    if len(walkable) == 0:
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
