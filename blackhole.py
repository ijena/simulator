# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from math import sqrt
from random import random


class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,2*Black_Hole.radius,2*Black_Hole.radius)
        
    def update(self, model):
        simultons_eaten = set()
        set_preys = model.find(lambda x:isinstance(x, Prey))
        for i in set_preys:
            if self.contains(i):
                model.remove(i)
                simultons_eaten.add(i)
        return simultons_eaten
                
        
    def display(self, canvas):
        canvas.create_oval(self._x-self.get_dimension()[0]/2     , self._y-self.get_dimension()[1]/2,
                               self._x+self.get_dimension()[0]/2, self._y+self.get_dimension()[1]/2,
                              fill="black")  
    def contains(self, prey_obj):
        if type(prey_obj) == tuple:
            return Simulton.contains(self, prey_obj)
        blackhole_center = self.get_location()
        prey_center = prey_obj.get_location()
        if  sqrt((blackhole_center[1]- prey_center[1])**2 + (blackhole_center[0]-prey_center[0])**2) < self.get_dimension()[0]/2:
            return True
        return False
        
