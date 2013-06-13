import sys
import pygame
import time
import math

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

if __name__ == "__main__":
  pygame.init()

  black = (0, 0, 0)
  size = width, height = 500, 500


  screen = pygame.display.set_mode(size)
  background = TiledSurface(size, 'grass.jpg')

  screen.blit(background, (0,0))
  pygame.display.flip()

  while 1:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
    
