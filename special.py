"""A special object is also a Prey object. It starts with a radius of 5 so a width and height of 10 and a speed of 25 pixels/update. The special object has 
a property of colors changing constantly randomly. This happens before start is even pressed. With every update, the width and height of the Special object
increases till it reaches a value of greater than 100 and then starts decreasing until it reaches any value lower than 10. Since it is a Prey object, it can
be "eaten" by a Blackhole, Pulsator or Hunter. The remove button can be used to remove a Special object too
"""
from prey import Prey
from math import pi
from random import random
from random import randint
increase=True
class Special(Prey): 
    radius = 5
    def random_color(self):
        rgb=[randint(0, 256), randint(0,256), randint(0,256)]
        return('#'+'{:x}{:x}{:x}'.format(rgb[0],rgb[1],rgb[2]))
    def increase_dimension(self):
        random_dimension=random()*10
        self.change_dimension(random_dimension,random_dimension)
    def decrease_dimension(self):
        random_dimension=random()*10
        self.change_dimension(-random_dimension,-random_dimension)    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,2*Special.radius,2*Special.radius,2*pi*random(), 25)
    def update(self, model):
        global increase
        global counter
        self.move()
        while self.get_dimension()[0]<=100 and increase==True:
            self.increase_dimension()
            break
        else:
            while self.get_dimension()[0]>=10:
                increase=False
                self.decrease_dimension()
                break
        if self.get_dimension()[0]<=10:
            increase =True
    def display(self, canvas):
        while True:    
            try:
                canvas.create_oval(self._x-self.get_dimension()[0]/2     , self._y-self.get_dimension()[1]/2,
                               self._x+self.get_dimension()[0]/2, self._y+self.get_dimension()[1]/2,
                                fill=self.random_color())
                break
            except:
                    continue