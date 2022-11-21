from random import randint
import enum
class Visitor:
    def __init__(self, self_id, name, height, weight):
        self.id = self_id
        self.stats = Stats(height, weight)
        self.name = name
        self.tickets = 0
        self.state = Visitor_state(0)
    

class Stats:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
class Visitor_state(enum.Enum):
    walks = 0
    in_queue = 1
    on_attraction = 2    
        