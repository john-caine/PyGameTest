import sys
import pygame
import time

def tile_screen(imagename): 
	image = pygame.image.load(imagename).convert()
	
	imagerect = image.get_rect()
	xtracker = 0
	ytracker = 0

	while xtracker < width or ytracker < height:
		screen.blit(image, imagerect)
	
		if ytracker > height:
			break
		elif xtracker > width:
			xtracker = 0
			ytracker = ytracker + image.get_height()
			imagerect = image.get_rect().move(xtracker, ytracker)		
		else:
			xtracker = xtracker + image.get_width()
			imagerect = image.get_rect().move(xtracker, ytracker)


if __name__ == "__main__":
	pygame.init()

	black = (0, 0, 0)
	size = width, height = 500, 500
				
	screen = pygame.display.set_mode(size)
	screen.fill(black)

	tile_screen('grass.jpg')
				
	pygame.display.flip()

	while 1:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		
