import pygame
pygame.init()
size=[400,300]
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()

done=False
while not done:
	# pass
	keys=pygame.key.get_pressed()
	if keys[pygame.K_w]:
		print 'hello'
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True

	clock.tick(32)
pygame.quit()
		