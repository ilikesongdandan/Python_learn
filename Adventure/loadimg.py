import pygame
pygame.init()

windowSize=[400,300]
screen=pygame.display.set_mode(windowSize)

img=pygame.image.load('thumb.jpg')
p1=pygame.image.load('1.png')
p2=pygame.image.load('2.png')

screen.blit(img,(0,0))
screen.blit(p1,(5,5))

done=False
while not done:
	# pass
	for even in pygame.event.get():
		if even.type==pygame.QUIT:
			done=True
	pygame.display.flip()
pygame.quit()