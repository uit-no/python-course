class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.age = 0
        self.pets_met = set()
        
    def advance_time(self):
        self.age += 1
        self.hunger += 1
        
    def feed(self):
        self.hunger = 0
        
    def meet(self, other_pet):
        print("{} meets {}".format(self.name, other_pet.name))
        self.pets_met.add(other_pet)
        other_pet.pets_met.add(self)
        
    def print_stats(self):
        print("{o.name}, age {o.age}, hunger {o.hunger}, met {n} others".
             format(o = self, n = len(self.pets_met)))
