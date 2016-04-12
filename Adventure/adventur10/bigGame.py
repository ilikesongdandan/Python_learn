import pygame
import random
pygame.mixer.init()
pygame.init()

def moveAction(image1,image2,count):
	if 10<count%20<=20:
		return image2
	else:
		return image1

def upClear(x,y):
	canMove=True
	if verticalDoorLeft<=x<=verticalDoorRight and y-1<topWall:
		canMove=True
	elif y-1<topWall:
		canMove=False
	elif (x<leftWall or x>rightWall) and y-1<middleDoorsTop:
		canMove=False

	if canMove:
		return 1
	else :
		return 0

def downClear(x,y):
	canMove=True
	if verticalDoorLeft<=x<=verticalDoorRight and y+1>bottomWall:
		canMove=True
	elif y+1>bottomWall:
		canMove=False
	elif (x<leftWall or x>rightWall) and y+1>middleDoorsBottom:
		canMove=False

	if canMove:
		return 1
	else :
		return 0

def leftClear(x,y):
	canMove=True

	if middleDoorsTop<=y<=middleDoorsBottom and x-1<leftWall:
		canMove=True
	elif x-1<leftWall:
		canMove=False
	elif (y>bottomWall or y<topWall) and x-1<verticalDoorLeft:
		canMove=False

	if canMove:
		return 1
	else :
		return 0

def rightClear(x,y):
	canMove=True

	if middleDoorsTop<=y<=middleDoorsBottom and x+1>rightWall:
		canMove=True
	elif x+1>rightWall:
		canMove=False
	elif (y>bottomWall or y<topWall) and x+1>verticalDoorRight:
		canMove=False

	if canMove:
		return 1
	else :
		return 0


def checkOffScreen(x,y):
	# pass
	if x<-14:
		x=windowSize[0]-14
	elif x>windowSize[0]-14:
		x=-14

	if y<-20:
		y=windowSize[1]-20
	elif y>windowSize[1]-20:
		y=-20
	return x,y



def playersTouching():
	# pass
	global pOneX,pOneY,pTwoX,pTwoY

	if -32<pOneX-pTwoX<32 and -40<pOneY-pTwoY<40 :
		xDiff=pOneX-pTwoX
		yDiff=pOneY-pTwoY

		for dist in range(abs(xDiff)/2):
			pOneMove=leftClear(pOneX, pOneY)+rightClear(pOneX, pOneY)
			pTwoMove=leftClear(pTwoX, pTwoY)+rightClear(pTwoX, pTwoY)
			if xDiff >0:
				pOneX+=pOneMove/2*xDiff/xDiff
				pTwox-=pTwoMove/2*xDiff/xDiff
			else :
				pOneX-=pOneMove/2*xDiff/xDiff
				pTwoX+=pTwoMove/2*xDiff/xDiff
		for dist in range(abs(yDiff)/2):
			pOneMove=upClear(pOneX, pOneY)+upClear(pOneX, pOneY)
			pTwoMove=upClear(pTwoX, pTwoY)+upClear(pTwoX, pTwoY)
			if yDiff>0:
				pOneY+=pOneMove/2*yDiff/yDiff
				pTwoY-=pTwoMove/2*yDiff/yDiff
			else :
				pOneY-=pOneMove/2*yDiff/yDiff
				pTwoY+=pTwoMove/2*yDiff/yDiff


def touchingCoin(x,y):
	# pass
	return -32<x-coinPos[0]<20 and -40<y-coinPos[1]<20

def randomPosition():
	# pass
	x=random.randrange(32,windowSize[0]-52)
	y=random.randrange(32,windowSize[1]-52)
	return x,y



windowSize=[640,384]
screen=pygame.display.set_mode(windowSize)
clock=pygame.time.Clock()

#Font for points
pointFont=pygame.font.SysFont('Monospace',15)

#variable for position etc
pOneX=windowSize[0]/4
pOneY=windowSize[1]/2

pTwoX=(windowSize[0]/4)*3
pTwoY=windowSize[1]/2

coinPos=randomPosition()

pOnePoints=0
pTwoPoints=0

pOneCount=0
pTwoCount=0

pOneMoving=False
pTwoMoving=False

#variabl for walls

leftWall=28
topWall=16
rightWall=windowSize[0]-60
bottomWall=312

middleDoorsTop=144
middleDoorsBottom=182
verticalDoorLeft=284
verticalDoorRight=verticalDoorLeft+40

background=pygame.image.load('background.png')
background=pygame.transform.scale(background,windowSize)

light=pygame.image.load('light.png')
light=pygame.transform.scale(light,windowSize)

pOneMove1=pygame.image.load('sprite1_walking1.png')
pOneMove1=pygame.transform.scale2x(pOneMove1)

pOneMove2=pygame.image.load('sprite1_walking2.png')
pOneMove2=pygame.transform.scale2x(pOneMove2)

pOneStanding=pygame.image.load('sprite1_standing.png')
pOneStanding=pygame.transform.scale2x(pOneStanding)

pTwoMove1=pygame.image.load('sprite2_walking1.png')
pTwoMove1=pygame.transform.scale2x(pTwoMove1)

pTwoMove2=pygame.image.load('sprite2_walking2.png')
pTwoMove2=pygame.transform.scale2x(pTwoMove2)

pTwoStanding=pygame.image.load('sprite2_standing.png')
pTwoStanding=pygame.transform.scale2x(pTwoStanding)

coin=pygame.image.load('coin.png')
coin=pygame.transform.scale2x(coin)

#load music and sound

CoinSound=pygame.mixer.Sound('coin.wav')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

#game loop
done=False
while not done:
	#get movement
	#pOne movement
	pOneMoving=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_s]:
		pOneY+=downClear(pOneX, pOneY)
		pOneMoving=True

	if keys[pygame.K_w]:
		pOneY-=upClear(pOneX, pOneY)
		pOneMoving=True
	if keys[pygame.K_a]:
		pOneX-=leftClear(pOneX, pOneY)
		pOneMoving=True
	if keys[pygame.K_d]:
		pOneX+=rightClear(pOneX, pOneY)
		pOneMoving=True

	pOneX,pOneY=checkOffScreen(pOneX, pOneY)

	#player 1 animation
	if pOneMoving :
		pOneCount+=1
		pOneImage=moveAction(pOneMove1, pOneMove2, pOneCount)
	else :
		pOneImage=pOneStanding

	#player 2 movement
	pTwoMoving=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_DOWN]:
		pTwoY+=downClear(pTwoX, pTwoY)
		pTwoMoving=True

	if keys[pygame.K_UP]:
		pTwoY-=upClear(pTwoX, pTwoY)
		pTwoMoving=True
	if keys[pygame.K_LEFT]:
		pTwoX-=leftClear(pTwoX, pTwoY)
		pTwoMoving=True
	if keys[pygame.K_RIGHT]:
		pTwoX+=rightClear(pTwoX, pTwoY)
		pTwoMoving=True

	pTwoX,pTwoY=checkOffScreen(pTwoX, pTwoY)

	#player 2 animation
	if pTwoMoving :
		pTwoCount+=1
		pTwoImage=moveAction(pTwoMove1, pTwoMove2, pTwoCount)
	else :
		pTwoImage=pTwoStanding

	#check touching
	playersTouching()

	#check touching coin
	if touchingCoin(pOneX, pOneY):
		pOnePoints+=1
		CoinSound.play()
	if touchingCoin(pTwoX, pTwoY):
		pTwoPoints+=1
		CoinSound.play()

	# move coin if touching
	if touchingCoin(pOneX, pOneY) or touchingCoin(pTwoX, pTwoY):
		coinPos=randomPosition()

	# render points for display

	pOnePointLabel=pointFont.render(str(pOnePoints),1,(255,255,255))
	pTwoPointLabel=pointFont.render(str(pTwoPoints),1,(255,255,255))

	#update display

	screen.blit(background,(0,0))
	screen.blit(coin,coinPos)
	screen.blit(pOneImage,[pOneX,pOneY])
	screen.blit(pTwoImage,[pTwoX,pTwoY])

	screen.blit(pOnePointLabel,[pOneX-9,pOneY-9])
	screen.blit(pTwoPointLabel,[pTwoX-9,pTwoY-9])

	screen.blit(light,(0,0))
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	clock.tick(60)
pygame.quit()