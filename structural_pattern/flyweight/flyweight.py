#!/usr/local/bin/python
# --*-- coding: utf-8 --*--

"""
share the same meta data
"""

import weakref
import six

class FlyweightMeta(type):
    def __new__(mcs, name, parents, attr):
        attr['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, attr)

    @classmethod
    def _seralize_params(cls, *args, **kwargs):
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        print ('call')
        key = cls._seralize_params(*args, **kwargs)
        pool = getattr(cls, 'pool', {})
        instance = pool.get(key)
        if instance is None:
            instance = super(FlyweightMeta, cls).__call__(cls, *args, **kwargs)
            pool[key] = instance
        return instance


class Card2(six.with_metaclass(FlyweightMeta)):
    def __init__(self, *args, **kwargs):
        pass

class Card(object):
    _CardPool = weakref.WeakValueDictionary()
    def __new__(cls, value, suit):
        print ('newr')
        obj = Card._CardPool.get(value+suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value+suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __init__(self, value, suit):
        print('111')

def main():
    card2_1 = Card2('a', '2')
    card2_2 = Card2('a', '2')
    print (id(card2_1), id(card2_2))

    card1_1 = Card('a', 'b')
    card1_2 = Card('a', 'b')

    print(id(card1_1), id(card1_2), type(card1_1), card1_1.value)


if __name__ == '__main__':
    main()
