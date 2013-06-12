import sys
import pygame
import time

pygame.init()

black = (0, 0, 0)

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

square = pygame.image.load('grass.jpg').convert()
#square2 = pygame.image.load('grass.jpg').convert()
squarerect = square.get_rect()
square2rect = square.get_rect().move(250, 0)

screen.fill(black)
screen.blit(square, squarerect)
screen.blit(square, square2rect)

pygame.display.flip()

a = 0

while a<50:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	a = a + 1
	time.sleep(1)
	
sys.exit(1)