#!/usr/local/bin/python
# --*-- coding:utf-8 --*--

"""
*What is this pattern about?
This pattern is used when creating an object is costly (and they are
created frequently) but only a few are used at a time. With a Pool we
can manage those instances we have as of now by caching them. Now it
is possible to skip the costly creation of an object if one is
available in the pool.
A pool allows to 'check out' an inactive object and then to return it.
If none are available the pool creates one to provide without wait.
*What does this example do?
In this example queue.Queue is used to create the pool (wrapped in a
custom ObjectPool object to use with the with statement), and it is
populated with strings.
As we can see, the first string object put in "yam" is USED by the
with statement. But because it is released back into the pool
aftwerwards it is reused by the explicit call to sample_queue.get().
Same thing happens with "sam", when the ObjectPool created insided the
function is deleted (by the GC) and the object is returned.
*Where is the pattern used practically?
*References:
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool
"""

class Pool(object):
    """
    use queue (thread safe) to store objects or connections
    using contexmanager to facilite
    """
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None


    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        # raise Exception('@@@@')
        return self.item

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None
        print( exc_type, exc_val)
        return True

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:
        import Queue as queue

    myqueue = queue.Queue()

    myqueue.put('A')
    myqueue.put('B')

    with Pool(myqueue) as p:
        print (p)
        print (pppp)

    print (myqueue.get())


if __name__ == '__main__':
    main()
