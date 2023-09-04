#!/usr/local/bin/python
# --*-- coding: utf-8 --*--

"""
adapt one interface to another using a white-list
*What is this pattern about?
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.
*What does this example do?
The example has classes that represent entities (Dog, Cat, Human, Car)
that make different noises. The Adapter class provides a different
interface to the original methods that make such noises. So the
original interfaces (e.g., bark and meow) are available under a
different name: make_noise.
*Where is the pattern used practically?
The Grok framework uses adapters to make objects work with a
particular API without modifying the objects themselves:
http://grok.zope.org/doc/current/grok_overview.html#adapters
*References:
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter
"""

class Dog(object):
    def __init__(self):
        self.name = 'dog'

    def bark(self):
        return 'woof'


class Car(object):
    def __init__(self):
        self.name = 'bmw'

    def make_noise(self, level):
        return 'vroom{}'.format("!"*level)

class Human(object):
    def __init__(self):
        self.name = 'moonmoonbird'

    def hello(self):
        return 'hello'

class Cat(object):
    def __init__(self):
        self.name = 'cat'

    def meow(self):
        return 'meow'


class Adapter(object):
    def __init__(self, obj, **adapter_method):
        self.obj = obj
        self.__dict__.update(adapter_method)

    def __getattr__(self, item):
        return getattr(self.obj, item)

    def origin_dict(self):
        return self.obj.__dict__


def main():
    objects = []
    cat = Cat()
    dog = Dog()
    car = Car()
    human = Human()
    objects.append(Adapter(cat, make_noise=cat.meow))
    objects.append(Adapter(dog, make_noise=dog.bark))
    objects.append(Adapter(car, make_noise=lambda:car.make_noise(3)))
    objects.append(Adapter(human, make_noise=human.hello))

    for obj in objects:
        print (obj.make_noise())


if __name__ == '__main__':
    main()