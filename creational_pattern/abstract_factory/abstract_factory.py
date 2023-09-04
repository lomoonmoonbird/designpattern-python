#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
*What is this pattern about?
The Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.
The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.
*What does this example do?
This particular implementation abstracts the creation of a pet and
does so depending on the AnimalFactory we chose (Dog or Cat)
This works because both Dog/Cat and their factories respect a common
interface (.speak(), get_pet() and get_food()).
Now my application can create pets (and feed them) abstractly and decide later,
based on my own criteria, dogs over cats.
The second example allows us to create pets based on the string passed by the
user, using cls.__subclasses__ (the list of sub classes for class cls)
and  sub_cls.__name__ to get its name.
*Where is the pattern used practically?
*References:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
"""

class PetShop(object):
    def __init__(self, animal_facitory=None):
        self.animal_factory = animal_facitory

    def show_pet(self):
        pet = self.animal_factory.get_pet()

        print("we have a lovely {name}".format(name=pet))
        print("It says {speak}".format(speak=pet.speak()))
        print("we also have {}".format(self.animal_factory.get_food()))


class Dog(object):
    def speak(self):
        return 'woof'

    def __str__(self):
        return "dog"

class Cat(object):
    def speak(self):
        return 'miao'

    def __str__(self):
        return 'cat'

class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return 'dog food'

class CatFactory(object):
    def get_pet(self):
        return Cat()
    def get_food(self):
        return 'cat food'

def get_factory(animal=None):
    if animal == 'cat':
        return CatFactory()
    elif animal == 'dog':
        return DogFactory()
    else:
        return None


if __name__ == "__main__":
    shop = PetShop(get_factory('cat'))
    shop.show_pet()
    print ("="*20)

    shop = PetShop(get_factory('dog'))
    shop.show_pet()
    print ("="*20)
