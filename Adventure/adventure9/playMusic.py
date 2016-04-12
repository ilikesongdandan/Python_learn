import pygame
pygame.mixer.init()
pygame.init()

clock=pygame.time.Clock()


crash=pygame.mixer.Sound('crash.wav')
hit=pygame.mixer.Sound('hit.wav')
# hit.play()

# pygame.time.wait(int(hit.get_length())*1000)

count=0
while  count<200:
	# pass
	if count%4==0:
		crash.play()
	else :
		hit.play()
	count+=1
	clock.tick(2)