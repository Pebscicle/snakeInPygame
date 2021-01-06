import pygame, random
import time

#Screen
screenWidth = 1080
screenHeight = 720

#GameSizes
snakeSize = 30

#Colors
grassColor  = (38,139,7)	
gridColor = (26, 97, 4)
snakeColor = (200, 15, 50)
appleColor = (0, 255, 0)

def placeApple():                           
	return [random.randint(0, screenWidth/snakeSize-1)*snakeSize, random.randint(0, screenHeight/snakeSize-1)*snakeSize]

def drawBoard():
	screen.fill(grassColor)
	pygame.draw.rect(screen, (170, 50, 50), (0, 0, screenWidth, screenHeight), 2)
	for i in range(36):
   		pygame.draw.line(screen, gridColor, (i*snakeSize+snakeSize, 0), (i*snakeSize+snakeSize, screenHeight), 1)
	for i in range(24):
		pygame.draw.line(screen, gridColor, (0, i*snakeSize+snakeSize), (screenWidth,i*snakeSize+snakeSize), 1)

x1 = 60
y1 = 60
class Snake:
  def __init__(self, x, y):
    self.x = [x1, x1-snakeSize, x1-snakeSize*2]
    self.y = [y1, y1, y1]
    self.prevX = [x1, x1-snakeSize, x1-snakeSize*2]
    self.prevY = [y1, y1-snakeSize, y1-snakeSize*2]

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight), 0, 32)
screen.fill(grassColor)

run= True
clock = pygame.time.Clock()
x1_change = snakeSize
y1_change = 0
score = 0
additionalSpeed = 0
appleCoords = placeApple()
font = pygame.font.SysFont('Arial', 20)
previousSnakeX = [x1]
previousSnakeY = [y1]
snake = Snake(x1, y1)

while run:
	#DRAW SCREEN
	drawBoard()
	#Draw apple
	pygame.draw.rect(screen, appleColor, (appleCoords[0], appleCoords[1], snakeSize, snakeSize))
	#DEAD IF BORDER
	if snake.x[0] < 0 or snake.x[0]>=screenWidth or snake.y[0]<0 or snake.y[0]>=screenHeight:
		run = False
	#MOVE SNAKE WHEN KEY PRESSED 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run=False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				x1_change = -snakeSize
				y1_change = 0
			elif event.key == pygame.K_RIGHT or event.key == ord('d'):
				x1_change = snakeSize
				y1_change = 0
			elif event.key == pygame.K_UP or event.key == ord('w'):
				y1_change = -snakeSize
				x1_change = 0
			elif event.key == pygame.K_DOWN or event.key == ord('s'):
				y1_change = snakeSize
				x1_change = 0
	for i in range(1, len(snake.x)):
		snake.prevX[i] = snake.x[i-1]
		snake.prevY[i] = snake.y[i-1]		
	#MOVE THE SNAKE HEAD
	snake.x[0] +=x1_change
	snake.y[0] += y1_change
	for i in range(1, len(snake.x)):
		snake.x[i] = snake.prevX[i]
		snake.y[i] = snake.prevY[i]
	for i in range(len(snake.x)):
		pygame.draw.rect(screen, (200, 15, 50), (snake.x[i], snake.y[i], snakeSize, snakeSize))
	#BUMP INTO TAIL
	for i in range(1, len(snake.x)):
		if (snake.x[0] == snake.x[i] and snake.y[0] == snake.y[i]):
			run = False
	#EAT APPLE
	if (snake.x[0] == appleCoords[0] and snake.y[0] == appleCoords[1]):
		appleCoords = placeApple()
		score+=1
		additionalSpeed+=0.15
		if snake.x[-1]-snake.x[-2]>0:
			snake.x.append(snake.x[-1]+snakeSize)
			snake.y.append(snake.y[-1])
		elif snake.x[-1]-snake.x[-2]<0:
			snake.x.append(snake.x[-1]-snakeSize)
			snake.y.append(snake.y[-1])
		if snake.y[-1]-snake.y[-2]>0:
			snake.y.append(snake.y[-1]+snakeSize)
			snake.x.append(snake.x[-1])
		elif snake.y[-1]-snake.y[-2]<0:
			snake.y.append(snake.y[-1]-snakeSize)
			snake.x.append(snake.x[-1])
		snake.prevX.append(0)
		snake.prevY.append(0)
	#Score 
	scoreText = font.render("Score: " + str(score) , False, (0, 0, 0))
	screen.blit(scoreText,(50,50))
	pygame.display.update()
	#Speed control
	clock.tick(5+additionalSpeed)
print("game over")
placeApple()
pygame.quit()