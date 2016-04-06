def make_dog_class():
    """
    Make a class `Dog` that satisfies the following conditions:
    * a dog has an attribute `happiness` which is initially set to 100, and
      which is decremented by 1 when time advances.
    * when a dog meets another dog, both dogs' happiness is reset to 100.
    * a dog is always hungrier than any other pet that is not a dog, regardless
      of the `hunger` attribute.
    * when a dog meets a fish, the dog is fed and the fish dies.
    """

    # The classes Pet and Fish are taken from the notebook. copy and paste (and
    # modify) them into the other exercises as you need them.
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


    Dog = None # define dog here

    return Pet, Fish, Dog


def test_dog_class():
    Pet, Fish, Dog = make_dog_class()
    assert type(Dog) == type
    d = Dog("Attila")
    assert hasattr(d, "happiness")
    assert d.happiness == 100
    d2 = Dog("Tamerlan")
    Pet.advance_time()
    assert d.happiness == d2.happiness == 99
    d.meet(d2)
    assert d.happiness == d2.happiness == 100
    f = Fish("Steve")
    f.hunger = 10
    assert d.hunger < f.hunger
    assert d.hungrier_than(f)
    assert d.hunger > 0
    d.meet(f)
    assert d.hunger == 0
    assert not f.is_alive()


###############################################################################

def define_hungry():
    """
    Copy the classes from the first exercise, and make the following happen:
    * all pets have an `is_hungry()` method which returns True if the animal is
      hungry, and False if not. in general, pets are considered to be hungry
      when their hunger is > 50.
    * there is a classmethod `Pet.get_hungry_pets()` which returns the set of
      pets that are currently hungry.
    """
    Pet = Fish = Dog = None

    return Pet, Fish, Dog


def test_define_hungry():
    Pet, Fish, Dog = define_hungry()

    p = Pet("p")
    f = Fish("f")
    d = Dog("d")
    assert isinstance(Pet.get_hungry_pets(), set)

    for x, h in [(p, 51), (f, 51), (d, 11)]:
        assert len(Pet.get_hungry_pets()) == 0
        assert not x.is_hungry()
        x.hunger = h
        assert x.is_hungry()
        assert Pet.get_hungry_pets() == {x}
        x.hunger = 0


# TODO make it so that fish and dog have their own population.
