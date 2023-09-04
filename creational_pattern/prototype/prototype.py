# --*-- coding:utf-8 --*--

"""
intent:
when object creation is time consuming, and costly operation, so we create object with existing object itself
1,Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
2,Co-opt one instance of a class for use as a breeder of all future instances.
3,The new operator considered harmful.

consist of:
1) Prototype : This is the prototype of actual object.

2) Prototype registry : This is used as registry service to have all prototypes accessible using simple string parameters.

3) Client : Client will be responsible for using registry service to access prototype instances.

when to use :
When a system should be independent of how its products are created, composed, and represented and
When the classes to instantiate are specified at run-time.
For example,
1) By dynamic loading or To avoid building a class hierarchy of factories that parallels the class hierarchy of products or

2) When instances of a class can have one of only a few different combinations of state.
It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually,
 each time with the appropriate state.

Advantages of Prototype Design Pattern:
1,Adding and removing products at run-time – Prototypes let you incorporate a new concrete product class into a system simply by registering a prototypical instance with the client.
That’s a bit more flexible than other creational patterns, because a client can install and remove prototypes at run-time.

2,Specifying new objects by varying values – Highly dynamic systems let you define new behavior
through object composition by specifying values for an object’s variables and not by defining new classes.

3,Specifying new objects by varying structure – Many applications build objects from parts and subparts. For convenience,
 such applications often let you instantiate complex, user-defined structures to use a specific subcircuit again and again

4,Reduced subclassing – Factory Method often produces a hierarchy of Creator classes that parallels the product class
hierarchy. The Prototype pattern lets you clone a prototype instead of asking a factory method to make a new object.
Hence you don’t need a Creator class hierarchy at all.

Disadvantages of Prototype Design Pattern:
1,Overkill for a project that uses very few objects and/or does not have an underlying emphasis on the extension of prototype chains.
2,It also hides concrete product classes from the client
3,Each subclass of Prototype must implement the clone() operation which may be difficult,
when the classes under consideration already exist. Also implementing clone() can be difficult when their internals
 include objects that don’t support copying or have circular references.
"""
class Prototype(object):
    value = ''
    def __init__(self):
        pass

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}


    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value= "a", b="b")
    b = prototype.clone(value="c",d="d")

    dispatcher.register_object('obja', a)
    dispatcher.register_object('objb', b)
    dispatcher.register_object('objd', d)

    print ( [{n: p.value} for n,p in dispatcher.get_objects().items()] )


if __name__ == '__main__':
    main()