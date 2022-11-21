from visitor import Visitor
import enum
class Attraction:
    def __init__(self, name: str, size: int, working_time: int, state: int = 0):
        self.name: str = name
        self.size: int = size
        self.state: int = state 
        self.working_time: int = working_time
        self.visitors = []
        self.state = Attraction_state(0)
        self.queue = Queue()
        pass
    
    def run(self):
        pass
    
    def add_visitor(self, v: Visitor):
        self.Visitors.append(v)
        
    def del_visitor(self, v: Visitor):
        self.visitors.remove(v)
        
    def add_visitor_to_queue(self,v: Visitor):
        self.queue.add_visitor(v)
        
    def del_visitor_from_queue(self,v: Visitor):
        self.queue.del_visitor(v)
        
        
class Attraction_state(enum.Enum):
    running = 1
    stopped = 0


class Queue:
    def __init__(self):
        self.visitors = []
        self.size = 0
        
    def add_visitor(self, v: Visitor):
        self.Visitors.append(v)
        
    def del_visitor(self, v: Visitor):
        self.visitors.remove(v)
        