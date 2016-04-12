import pygame
import math
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

count=0
while pygame.mixer.music.get_busy():
	# pygame.time.wait(200)
	# for event in pygame.event.get():
	# 	if event.type==pygame.QUIT:
	# 		done=True
	volume=abs(math.sin(count))
	pygame.mixer.music.set_volume(volume)
	count+=0.2
	print volume
	pygame.time.delay(200)
# pygame.quit()