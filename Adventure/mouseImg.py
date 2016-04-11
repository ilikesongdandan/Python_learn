import pygame
pygame.init()
windowSize=[400,300]
screen=pygame.display.set_mode(windowSize)

bg=pygame.image.load('thumb.jpg')
p1=pygame.image.load('images/down1.png')

black=pygame.color.Color('#000000')

bgpos=(0,0)
pos=(0,0)
screen.blit(bg,bgpos)

done=False
while not done:
	# pass
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			pos=pygame.mouse.get_pos()
			screen.fill(black)
			screen.blit(bg,bgpos)
			screen.blit(p1,pos)
		if event.type==pygame.QUIT:
			# pass
			done=True
	pygame.display.flip()
pygame.quit()