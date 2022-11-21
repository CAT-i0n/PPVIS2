from view import View
from attraction import Attraction
from visitor import Visitor
from random import randint
from name_gen import *
class Park:
    def __init__(self):
        self.attractions = []
        self.visitors = []
        self.prepare_data()
        self.view = View(self)
        self.name = ''
        
    def run(self):
        pass
    
    def prepare_data(self, data = None):
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
        
        for i in self.attractions:
            for _ in range(randint(2,10)):
                v = Visitor(randint(0, 10000), generate(), randint(100, 200), randint(30,100))
                self.visitors.append(v)
                i.add_visitor_to_queue(v)
    
    def add_to_queue(self, *args, **kwargs):
        pass
    
    def run_attraction(self, *args, **kwargs):
        pass
    
    def del_from_queue(self, *args, **kwargs):
        pass
    
    def add_tickets(self, *args, **kwargs):
        pass
    
    def save_data(self, *args, **kwargs):
        pass
    
    def add_visitor(self, *args, **kwargs):
        pass
    
    def del_visitor(self, *args, **kwargs):
        pass
    
    def change_tickets(self, *args, **kwargs):
        pass
    
    def get_visitor_data(self, *args, **kwargs):
        pass
    
    