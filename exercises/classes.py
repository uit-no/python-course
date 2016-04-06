def make_dog_class():
    """
    Make a class `Dog` that satisfies the following conditions:
    * a dog has an attribute `happiness` which is initially set to 100, and
      which is decremented by 1 when time advances.
    * when a dog meets another dog, both dogs' happiness is reset to 100.
    * when a dog meets a fish, the dog feeds and the fish dies.
      * Note: "when a dog meets a fish" need not have the same effect as "when
        a fish meets a dog" - but extra kudos to you if you can make it so.
    """

    # The classes Pet and Fish are taken from the notebook. copy and paste (and
    # modify) them into the other exercises as you need them.
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
	def __init__(self, name, size):
	    self.size = size
	    super().__init__(name)
	    
	def meet(self, other_fish):
	    super().meet(other_fish)
	    if not isinstance(other_fish, Fish):
		return
	    if self.size > other_fish.size:
		self.feed()
		other_fish.die()
	    elif self.size < other_fish.size:
		other_fish.feed()
		self.die()


    Dog = None # make Dog class here

    return Pet, Fish, Dog


def test_dog_class():
    Pet, Fish, Dog = make_dog_class()
    assert type(Dog) == type

    attila = Dog("Attila")
    assert hasattr(attila, "happiness")
    assert attila.happiness == 100

    tamerlan = Dog("Tamerlan")

    Pet.advance_time()
    assert attila.happiness == tamerlan.happiness == 99

    attila.meet(tamerlan)
    assert attila.happiness == tamerlan.happiness == 100
    assert attila in tamerlan.pets_met
    assert tamerlan in attila.pets_met

    steve = Fish("Steve")

    assert attila.hunger > 0
    attila.meet(steve)
    assert attila.hunger == 0
    assert not steve.is_alive()


###############################################################################

def define_hungry():
    """
    Copy your classes from the first exercise, and make the following happen:
    * all pets have an `is_hungry()` method which returns True if the animal is
      hungry, and False if not. In general, pets are considered to be hungry
      when their hunger is > 50. Dogs, however, are considered to be hungry
      when their hunger is > 10.
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
