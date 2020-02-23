class spaceship:
    
    def __init__(self, x, y, speed, acc=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.acc = acc
        
    def acceleration(self):
        self.speed += self.acc
        
    def moving(self):
        self.x += self.speed
