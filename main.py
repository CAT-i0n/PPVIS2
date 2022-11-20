from park import Park
class Application:
    def __init__(self):
        self.park = Park()
        
    def main(self):
        self.park.run()
        
        
if __name__ == "__main__":
    Application().main() 