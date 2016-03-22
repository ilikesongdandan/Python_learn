import math
import pygame
import random
pygame.init()
windowSize=[400,300]
screen=pygame.display.set_mode(windowSize)
clock=pygame.time.Clock()

width=200
height=200
x=windowSize[0]/2-width/2
y=windowSize[1]/2-height/2

color=pygame.color.Color('#57b0f6')
black=pygame.color.Color('#000000')

count=0
done=False
while not done:
	# pass
	screen.fill(black)

	pygame.draw.ellipse(screen,color,[x,y,width,height])

	color[0]=random.randrange(0,256,1)
	color[1]=random.randrange(0,256,1)
	color[2]=random.randrange(0,256,1)
	width+=math.cos(count)*10
	x-=(math.cos(count)*10)/2
	height+=math.sin(count)*10
	y-=(math.sin(count)*10)/2
	count+=0.5

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	clock.tick(24)
pygame.quit()