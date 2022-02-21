from fei.ppds import Thread, Mutex
from collections import Counter

mutex = Mutex()


class Shared:
    '''
    Shared class that has the following attributes:
    1. counter
    2. field size end
    3. an integer field of end size with zeroed elements
    '''
    def __init__(self, size):
        self.counter = 0
        self.end = size
        self.elms = [0] * (size + 10)


def do_count(shared):
    '''
    Function that takes a shared object as an argument.
    This function will be performed by threads.
    '''
    mutex.lock()
    while shared.counter < shared.end:
        shared.elms[shared.counter] += 1
        shared.counter += 1
    mutex.unlock()


shared = Shared(10000000)
t1 = Thread(do_count, shared)
t2 = Thread(do_count, shared)
t1.join()
t2.join()

counter = Counter(shared.elms)
print(counter.most_common())
