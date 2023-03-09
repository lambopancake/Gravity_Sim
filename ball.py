import pygame, math, random, time

class ball:
	def __init__(self, screen, color,
				x, y, velocity = 0, accel = 1, angle = 0, decel = 100 ):
		self.screen = screen
		self.color = color
		self.pos = [x, y]
		self.velocity = velocity	
		self.angle = angle
		self.accel = accel * -1
		self.decel = decel
		self.y_comp = self.velocity * math.sin(math.radians(self.angle)) 
		self.x_comp = self.velocity * math.cos(math.radians(self.angle))
		self.size = random.randint(10,25)
		self.shadowArr = []



	def changePoints(self):
		self.pos = [self.pos[0] + self.x_comp ,self.pos[1] + self.y_comp]

	def changeVel(self, t):
		#true changes the x_comp
		#false changes the y_comp
		#c is the the percent lost in each bounce 
		#if c == 100 does lose anything 90 loses 10%
		if(t == True):
			self.x_comp *= -1
		else:
			a = 0.99653 * (self.decel * 0.01)

			self.y_comp *= -a
			print(self.y_comp)

	
	def gravity(self):
		self.y_comp -= self.accel * 0.001

	def bounds(self, size):
		if(self.pos[1] <= 50 and self.y_comp < 0):
			self.changeVel(False)
			
		if(self.pos[1] >= size - 50 and self.y_comp > 0):
			self.changeVel(False)

		if(self.pos[0] > size - 50 or self.pos[0] < 50):
			self.changeVel(True)

	def draw(self):
		pygame.draw.circle(self.screen,self.color,(self.pos[0],self.pos[1]),self.size,0)
		
	def main(self, a):
		self.changePoints()
		self.gravity()
		self.shadow()
		self.draw()
		self.bounds(a)

	def shadow(self):
		if(len(self.shadowArr) > 20):
			self.shadowArr.pop()
		for i in range(len(self.shadowArr)):
			pygame.draw.circle(self.screen, "BLUE",(self.shadowArr[i][0],self.shadowArr[i][1]),self.size - i,0)
	
	def calcVector(self):
		#returns [speed, angle]
		
		speed = math.hypot(self.x_comp, self.y_comp)
		angle = math.degrees(math.tan(self.y_comp / self.x_comp))
		return [speed, angle]



		
if __name__ == '__main__':
	a = 800
	screen = pygame.display.set_mode((a,a))
	screen.fill((123,28,89))

	x = 350
	y = 350

	# ball = ball(screen,"GREEN", x, y, velocity = random.randint(0,100) * 0.01 ,
	# 						 accel = random.randint(0, 10),decel = random.randint(60,100), angle = random.randint(0,360))
	
	ball1 = ball(screen,"GREEN", x, y, velocity = 0, accel = 1,decel = 100, angle = 90)
	
	# print(ball.y_comp, " ", ball.x_comp)
	# print((ball.y_comp/ball.x_comp))
	# print(math.tan(ball.y_comp/ball.x_comp))
	#print(ball.__dict__)
	count = 0
	while True:
		
		pygame.time.delay(1)
		screen.fill((123,28,89))
		
		ball1.main(a)
		if(count > 20):
			ball1.shadowArr.insert(0,[ball1.pos[0],ball1.pos[1]])
			count = 0
		count += 1
		# time.sleep(.1)
		#print(ball.calcVector())


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()