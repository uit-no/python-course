class Pet:
    population = set()
    
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.age = 0
        self.pets_met = set()
        self.__class__.population.add(self)
        
    def die(self):
        print("{} dies :(".format(self.name))
        self.__class__.population.remove(self)
        
    def is_alive(self):
        return self in self.__class__.population
        
    @classmethod
    def advance_time(cls):
        for pet in cls.population:
            pet.age += 1
            pet.hunger += 1
        
    def feed(self):
        self.hunger = 0
        
    def meet(self, other_pet):
        print("{} meets {}".format(self.name, other_pet.name))
        self.pets_met.add(other_pet)
        other_pet.pets_met.add(self)
        
    def print_stats(self):
        print("{o.name}, age {o.age}, hunger {o.hunger}, met {n} others".
             format(o = self, n = len(self.pets_met)))


class Fish(Pet):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)
        
    def meet(self, other_fish):
        if not isinstance(other_fish, Fish):
            return
        if self.color != other_fish.color:
            if self.hungrier_than(other_fish):
                self.feed()
                other_fish.die()
            elif other_fish.hungrier_than(self):
                other_fish.feed()
                self.die()
