from view import View
from attraction import Attraction
class Park:
    def __init__(self):
        self.attractions = []
        self.prepare_data()
        self.view = View(self)
        
    def run(self):
        pass
    
    def prepare_data(self):
        self.attractions.append(Attraction(name = 'Американские гонки', 
                                size = 10, working_time = 30))
        self.attractions.append(Attraction(name = 'Мини-поезд', 
                                size = 10, working_time = 30))
        self.attractions.append(Attraction(name = 'Парусник', 
                                size = 10, working_time = 30))
        self.attractions.append(Attraction(name = 'Качели', 
                                size = 10, working_time = 30))
        self.attractions.append(Attraction(name = 'Батуты', 
                                size = 10, working_time = 30))
        self.attractions.append(Attraction(name = 'Электромашины', 
                                size = 10, working_time = 30))
        
        pass
    
    def save_data(self):
        pass