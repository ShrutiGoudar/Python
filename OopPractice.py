#Write Class Line , add methods to accept coordinates as tuplesand return the slope and distance of line
# dist = sqrt((y2-y1)**2 + (x2-x1)**2)
#slope = (y2-y1)/(x2-x1)
import math

class point : 
    #attributes
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_point(self):
        return (self.x, self.y)
    
    def __str__(self):
        return "Point ({},{})".format(self.x,self.y)



class Line():
    #attributes
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2

    def get_distance(self):
        dist = math.sqrt((self.p2.y - self.p1.y)**2 + (self.p2.x - self.p1.x)**2)
        return dist

    def slope(self):
        slope = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
        return slope


p1 = point(1,1)
p2 = point(0,0)
line = Line(p1,p2)
print(line.get_distance())