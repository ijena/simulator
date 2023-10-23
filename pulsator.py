# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    death_counter = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.time_between_meals = 0
    def update(self, model):
        simultons_eaten = Black_Hole.update(self, model)
        if simultons_eaten != set():
            self.change_dimension(len(simultons_eaten),len(simultons_eaten))
            self.time_between_meals = 0
        else:
            self.time_between_meals+=1
            if Pulsator.death_counter==self.time_between_meals:
                self.change_dimension(-1,-1)
                self.time_between_meals=0
            if self.get_dimension()==(0,0):
                model.remove(self)
        return simultons_eaten