# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
 
from prey import Prey
from math import pi
import random
class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,2*Floater.radius,2*Floater.radius,2*pi*random.random(), 5)
    def update(self, model):
        speed_angle_change = random.randint(1, 10)
        if speed_angle_change <= 3:
            temp_speed = self.get_speed()+ random.random()- 0.5
            if temp_speed <3:
                self.set_speed(3)
            elif temp_speed > 7:
                self.set_speed(7)
            else:
                self.set_speed(temp_speed)
            self.set_angle(self.get_angle()+ random.random()-0.5)
        self.move()
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill="red")
        