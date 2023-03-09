import pygame, random
from ball import ball
from tkinter import *
import threading


a =800

screen = pygame.display.set_mode((a,a))
#pygame.display.flip()
screen.fill((24,78,90))

running = True
x = 350
y = 350

colorArr = ["GREEN", "BLUE","RED","PURPLE","BLACK","YELLOW"]

vecArr = []
for _ in range(1):
	x = random.randint(100,600)
	y = random.randint(300,600)
	vecArr.append(ball(screen,random.choice(colorArr), x, y, velocity = random.randint(0,100) * 0.01 ,
							 accel = 0,decel = random.randint(60,100), angle = random.randint(0,360)))
	#print(vecArr[-1].__dict__)

vecArr[0] = ball(screen,"GREEN", x, 350, velocity = 0, accel = 9.8,decel = 100, angle = 0)
gravity = 0
def printG(a):
	global gravity
	gravity = float(a) * -1

resistance = 0
def printR(a):
	global resistance
	resistance = float(a)

def slider():
	print('running')
	m = Tk()
	g = Scale(m, label = "gravity", from_ = 10, to = -10, resolution = 0.1, command = printG)
	g.set(0)
	g.pack()
	a = Scale(m, label = "Air resistance", from_ = 100, to = 0, command = printR)
	a.set(100)
	a.pack()

	mainloop()

t1 = threading.Thread(target = slider)
t1.start()

print(vecArr[0].__dict__)	
while running:
	
	

	#pygame.time.delay(1)
	screen.fill((24,78,90))

	for ball in range(len(vecArr)):
		##############################################
		vecArr[ball].accel = gravity
		vecArr[ball].decel = resistance
		#print(resistance)
		#print(type(gravity))
		vecArr[ball].main(a)


		############################################
		
	

	##############################################
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		
			running = False
				
	pygame.display.update()
	##############################################
