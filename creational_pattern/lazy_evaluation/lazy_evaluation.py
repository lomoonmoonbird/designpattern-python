# --*-- coding: utf-8 --*--

"""
lazy evaluation with python descriptor which defined __get__ __set__ __delete__ method
"""

import functools

class lazy_property(object):
    """
    defined as descriptor
    """
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, self.func)

    def __get__(self, instance, owner):
        val = self.func(instance)
        instance.__dict__[self.func.__name__] = val
        return val


def lazy_property_normal(func):
    """
    non descriptor
    :param func:
    :return:
    """
    attr = '_lazy_'+func.__name__

    @property
    @functools.wraps(func)
    def _lazy_property_normal(self):
        if not hasattr(self, attr):
            setattr(self, attr, func(self))
        return getattr(self, attr)

    return _lazy_property_normal


class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    @lazy_property
    def get_name(self):
        return  'name'

    @lazy_property_normal
    def get_age(self):
        return 11

if __name__ == '__main__':
    p = Person('jinpeng', 24)

    print ('before:')
    print (p.__dict__)
    print ( p.get_name )
    print ('after:')
    print (p.__dict__)


    print ('before:')
    print (p.__dict__)
    print ( p.get_age )
    print ('after:')
    print (p.__dict__)
