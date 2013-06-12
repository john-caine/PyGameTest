import sys
import pygame
import time

pygame.init()

black = (0, 0, 0)

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

grass = pygame.image.load('grass.jpg').convert()

screen.fill(black)
grassrect = grass.get_rect()
xtracker = 0
ytracker = 0

while xtracker < width or ytracker < height:
	screen.blit(grass, grassrect)
	
	if ytracker > height:
		break
	elif xtracker > width:
		xtracker = 0
		ytracker = ytracker + grass.get_height()
		grassrect = grass.get_rect().move(xtracker, ytracker)		
	else:
		xtracker = xtracker + grass.get_width()
		grassrect = grass.get_rect().move(xtracker, ytracker)
			
pygame.display.flip()

while 1:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()