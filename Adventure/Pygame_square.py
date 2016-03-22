import pygame
pygame.init()
width=400
height=300
windowSize=[width,height]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption('rect')
color=pygame.color.Color('#646400')
row=0
done=False
while  not done:
	# pass
	increment=255/100
	while row<height:
		pygame.draw.rect(screen,color,[0,row,width,row+increment])
		pygame.display.flip()
		if color[2]+increment<255:
			color[2]+=increment
		row+=increment
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
pygame.quit()
		# pass