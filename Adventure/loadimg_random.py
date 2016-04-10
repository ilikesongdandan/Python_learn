import pygame
import random
pygame.init()

windowSize=[400,300]
screen=pygame.display.set_mode(windowSize)
clock=pygame.time.Clock()

bgimg=pygame.image.load('bg.jpg')
p1=pygame.image.load('1.png')

screen.blit(bgimg,(0,0))
done=False
while not done:
	# pass
	x=random.randint(0, windowSize[0])
	y=random.randint(0, windowSize[1])
	angle=random.randint(0, 360)
	rotatedImg=pygame.transform.rotate(p1,angle)
	screen.blit(rotatedImg,(x,y))
	for even in pygame.event.get():
		if even.type==pygame.QUIT:
			done=True
	pygame.display.flip()
	clock.tick(10)
pygame.quit()