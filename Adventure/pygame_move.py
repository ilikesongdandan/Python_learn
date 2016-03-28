import pygame
import random

pygame.init()
size=[400,300]
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()

x=size[0]/2
y=size[1]/2

red=pygame.color.Color('#FF8080')
blue=pygame.color.Color('#8080FF')
white=pygame.color.Color('#ffffff')
black=pygame.color.Color('#000000')

ballx=random.randrange(0,size[0])
bally=random.randrange(0,size[1])
#goal position
goalx=size[0]/2
goaly=size[1]/2
goalr=20


points=0



def checkofsizex(x):
	if x>size[0]:
		x=0
	elif x<0:
		x=size[0]
	return x

def checkofsizey(y):
	if y>size[1]:
		y=0
	elif y<0:
		y=size[1]
	return y

def checkTouch():
	global x
	global y
	global ballx
	global bally
	# draw an explosion
	if -10<y-bally<10 and -10<x-ballx<10:
		pygame.draw.circle(screen,white,[x,y],15)

		xDiff=x-ballx
		yDiff=y-bally
		# check if ball is on edge of screen
		if ballx==0: 
			xDiff-=5
		elif ballx==size[0]:
			xDiff+=5
		if bally==0:
			yDiff-=5
		elif bally==size[1]:
			yDiff+=5
		# move the ball and palyer
		x+=xDiff*3
		ballx-=xDiff*3

		y+=xDiff*3
		bally-=yDiff*3


done=False
timeStart=pygame.time.get_ticks()
while not done:
	screen.fill(black)
	pygame.draw.circle(screen,white,[goalx,goaly],goalr)
	# pygame.draw.rect(screen,white,(0,12,60,7))
	#check ball in goal
	# if goalx<=ballx<=goalx+goalw and goaly<bally<goaly+goalh:
	if -goalr<=ballx-goalx<=goalr and -goalr<=bally-goaly<=goalr:
		points+=1
		ballx=random.randrange(0,size[0])
		bally=random.randrange(0,size[1]) 

	keys=pygame.key.get_pressed()

	if keys[pygame.K_w]:
		y-=1
	if keys[pygame.K_s]:
		y+=1
	if keys[pygame.K_a]:
		x-=1
	if keys[pygame.K_d]:
		x+=1
	x=checkofsizex(x)
	y=checkofsizey(y)

	pygame.draw.circle(screen,red,[x,y],6)

	checkTouch()
	for point in range(points):
		pointX=0+point*5
		pygame.draw.rect(screen,white,(pointX,3,4,7))

	#ball posion
	pygame.draw.circle(screen,blue,[ballx,bally],6)
	ballx=checkofsizex(ballx)
	bally=checkofsizey(bally)

	timeNow=pygame.time.get_ticks()
	timeErr=timeNow-timeStart
	pygame.draw.rect(screen,white,(0,12,60-timeErr/1000,7))
	pygame.display.flip()
	# pygame.draw.rect(screen,white,(0,12,60,7))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	clock.tick(72)
	

	if timeErr>=60000:
		done=True
	# else:


pygame.quit()
print 'total points:'+str(points)