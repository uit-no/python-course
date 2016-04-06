class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.age = 0
        
    def advance_time(self):
        self.age += 1
        self.hunger += 1
        
    def feed(self):
        self.hunger = 0
        
    def hungrier_than(self, other_pet):
        return self.hunger > other_pet.hunger
