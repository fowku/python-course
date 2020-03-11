from abc import ABC, abstractmethod


class Animal(ABC):
    '''Животное'''

    def __init__(self, size, weight):
        self._size = size
        self._weight = weight

    @property
    @abstractmethod
    def is_angry(self):
        pass

    def get_size(self):
        return self._size

    def get_weight(self):
        return self._weight


class Chordate(Animal):
    '''Хордовое'''
    pass


class Mammal(Chordate):
    '''Млекопитающие'''
    pass


class Carnivora(Mammal):
    '''Хищник'''
    pass


class Canidae(Carnivora):
    '''Псовые'''
    pass


class Canis(Canidae):
    '''Волки'''
    pass


class Wolf(Canis):
    '''Волк'''

    def is_angry(self):
        return True


class Dog(Wolf):
    '''Собака'''

    def is_angry(self):
        return False


class GoldenRetriever(Dog):
    '''Золотистый ретривер'''

    def has_gold_furr(self):
        return True


wolf = Wolf(4, 12)
print(wolf.get_size())
print(wolf.get_weight())
print(wolf.is_angry())

print('\n')

doge = GoldenRetriever(4, 10)
print(doge.get_size())
print(doge.get_weight())
print(doge.is_angry())
print(doge.has_gold_furr())
