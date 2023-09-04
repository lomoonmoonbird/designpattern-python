#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.
*What does this example do?
To understand the implementation of this pattern in Python, it is
important to know that, in Python, instance attributes are stored in a
attribute dictionary called __dict__. Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.
In this example, the __shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
__shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is __shared_state), all other
attributes will also be shared.
For this reason, when the attribute self.state is modified using
instance rm2, the value of self.state in instance rm1 also chages. The
same happends if self.state is modified using rm3, which is an
instance from a subclass.
Notice that even though they share attributes, the instances are not
the same, as seen by their ids.
*Where is the pattern used practically?
Sharing state is useful in applications like managing database connections:
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py
*References:
https://fkromer.github.io/python-pattern-references/design/#singleton
"""

class Borg(object):
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        self.state = 'None'

    def __str__(self):
        return self.state


class Boarg1(Borg):
    pass


if __name__ == '__main__':
    b1 = Borg()
    b2 = Borg()

    b1.state = 'Idle'
    b2.state = 'Running'

    print('b1: {}'.format(b1))
    print('b2: {}'.format(b2))

    b2.state = 'zombie'

    print('b1: {}'.format(b1))
    print('b2: {}'.format(b2))

    print('id_b1: {}'.format(id(b1)))
    print('id_b2: {}'.format(id(b2)))

    b3 = Boarg1()
    print('b1: {}'.format(b1))
    print('b2: {}'.format(b2))
    print('b3: {}'.format(b3))

