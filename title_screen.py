import sys
import pygame

from constants import *

def run(screen):
  running = True
  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          sys.exit()
        elif event.key == pygame.K_RETURN:    
          running = False
          
    font = pygame.font.Font(None, 36)    
    title_text = font.render(TITLE_STRING, True, RED)
    textpos = title_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
    screen.blit(title_text, textpos)

    pygame.display.flip()
