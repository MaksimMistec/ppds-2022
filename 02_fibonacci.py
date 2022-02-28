from fei.ppds import Thread, Semaphore, Event, Mutex
from random import randint
from time import sleep


class Adt:
    """
    Class used to simulate barriers using events
    Function wait is used to stop barriers
    Function release is used to unblock barriers
    """
    def __init__(self, n):
        self.n = n
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.counter += 1
        if self.counter == self.n:
            self.event.signal()
        else:
            self.event.wait()

    def release(self):
        self.event.signal()


def compute_fibonacci(barrier, i):
    """
    Function used for calculating fibonacci's sequence
    Intended to be used with threads in this exercise
    """
    sleep(randint(1, 10)/10)
    barrier.wait()
    fib_seq[i+2] = fib_seq[i] + fib_seq[i+1]
    barrier.release()

THREADS = 10
fib_seq = [0] * (THREADS + 2)
fib_seq[1] = 1

adt = Adt(THREADS)
threads = [Thread(compute_fibonacci, adt, i) for i in range(THREADS)]
[t.join() for t in threads]

print(fib_seq)
