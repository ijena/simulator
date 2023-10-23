# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from random import random
from math import atan2
from math import pi
from math import sqrt


class Hunter(Pulsator, Mobile_Simulton): 
    distance = 200 
    def __init__(self, x, y):
        Pulsator.__init__(self, x,y)
        Mobile_Simulton.__init__(self, x,y, 20, 20, random()*2*pi, 5)
    def update(self, model):
        distance_list=[]
        simultons_eaten= Pulsator.update(self, model)
        Mobile_Simulton.move(self)
        Mobile_Simulton.wall_bounce(self)
        set_preys = model.find(lambda x:isinstance(x, Prey))
        for i in set_preys:
            prey_location = i.get_location()
            hunter_location = self.get_location()
            if  sqrt((hunter_location[1]- prey_location[1])**2 + (hunter_location[0]-prey_location[0])**2) < Hunter.distance:
                distance_list.append(sqrt((hunter_location[1]- prey_location[1])**2 + (hunter_location[0]-prey_location[0])**2))
        if len(distance_list)!=0:
            for i in set_preys:
                prey_location = i.get_location()
                hunter_location = self.get_location()
                if  sqrt((hunter_location[1]- prey_location[1])**2 + (hunter_location[0]-prey_location[0])**2) == min(distance_list):
                    self.set_angle(atan2(prey_location[1]-hunter_location[1], prey_location[0]-hunter_location[0]))
                    
            
                
                
            
            
            
