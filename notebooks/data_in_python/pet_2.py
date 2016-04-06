class Pet:
    population = set()
    
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.age = 0
        self.__class__.population.add(self)
        
    def die(self):
        print("{} dies :(".format(self.name))
        self.__class__.population.remove(self)
        
    def is_alive(self):
        return self in self.__class__.population
        
    @classmethod
    def advance_time(cls):
        for individual in cls.population:
            individual.age += 1
            individual.hunger += 1
        
    def feed(self):
        self.hunger = 0
        
    def hungrier_than(self, other_pet):
        return self.hunger > other_pet.hunger


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
