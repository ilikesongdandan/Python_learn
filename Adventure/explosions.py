import pygame
import random

pygame.init()

def randColor():
	r=random.randint(0, 255)
	g=random.randint(0, 255)
	b=random.randint(0, 255)
	return (r,g,b)

windowSize=[400,300]
screen=pygame.display.set_mode(windowSize)
clock=pygame.time.Clock()

black=pygame.color.Color('#000000')
color=randColor()

count=0
click=False

limit=30
pos=(0,0)

done=False

while  not done:
	screen.fill(black)

	if click and count<limit:
		pygame.draw.circle(screen,color,pos,count)
		count+=1
	# pass
		if count >=limit:
			click=False
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			pos=pygame.mouse.get_pos()
			click=True
			count=0
			color=randColor()
			# print pos
		if event.type==pygame.QUIT:
			done=True
	pygame.display.flip()
	clock.tick(60)
pygame.quit()