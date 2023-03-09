import pygame, math, random

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
			a = 0.9956 * (self.decel * 0.01)

			self.y_comp *= -a

	
	def gravity(self):
		self.y_comp -= self.accel * 0.001

	def draw(self):
		pygame.draw.circle(self.screen,self.color,(self.pos[0],self.pos[1]),self.size,0)
		

