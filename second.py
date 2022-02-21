from fei.ppds import Thread, Mutex
from collections import Counter

mutex = Mutex()


class Shared:

    def __init__(self, size):
        self.counter = 0
        self.end = size
        self.elms = [0] * (size + 10)


def do_count(shared):
    while shared.counter < shared.end:

        # shared.end - 1 to prevent last thread from incrementing an element
        #  past bounds, resulting in out of range error and checking
        # if our list doesn't contain just 1 element, otherwise this
        #  solution would instantly break in this case

        if shared.counter == shared.end - 1 and shared.end > 1:
            break
        mutex.lock()
        shared.elms[shared.counter] += 1
        shared.counter += 1
        mutex.unlock()


shared = Shared(1000000)
t1 = Thread(do_count, shared)
t2 = Thread(do_count, shared)
t1.join()
t2.join()

counter = Counter(shared.elms)
print(counter.most_common())
