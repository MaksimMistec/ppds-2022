#####################################################################
#
# File name: 05_savages.py
# Author: Maksim Mištec
# Creation date: 03/21/2022
# License: MIT
# Purpose: extension of exercise savages #1, where there will be
# multiple cooks, instead of just one. The cooks are to simultaneously
# prepare food, and once it's finished, the last cook will let the
# hungry savages know.
#
######################################################################
from random import randint
from time import sleep
from fei.ppds import Thread, print, Semaphore, Mutex, Event


"""
N = number of savages
M = number of portions to be cooked
C = number of cooks
"""
N = 3
M = 5
C = 4


class SimpleBarrier(object):
    """
    Barrier that is used to stop singular cooks
    from cooking multiple times before the other
    cooks finish cooking.
    """
    def __init__(self, N):
        self.N = N
        self.cnt = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        self.mutex.lock()
        self.cnt += 1
        if each:
            print(each)
        if self.cnt == self.N:
            if last:
                print(last)
            self.cnt = 0
            self.barrier.signal(self.N)
        self.mutex.unlock()
        self.barrier.wait()


class Shared(object):
    """
    Shared class we use for both savages and cooks.
    """
    def __init__(self, m):
        self.mutex = Mutex()
        self.mutex_cook = Mutex()
        self.servings = m
        self.full_pot = Semaphore(0)
        # using Event instead of Semaphor because
        # we want all cooks to start cooking
        self.empty_pot = Event()
        self.cooks_finished = 0
        self.barrier = SimpleBarrier(C)


def eat(i):
    """
    Simple function we use to show that a certain
    savage is eating, helps us to track if all
    savages got to eat, or if some were left behind.
    """
    print(f'savage {i} is eating')
    sleep(randint(50, 200) / 100)


def savage(i, shared):
    """
    Function for savages, if pot with food is empty, they
    wake all cooks up and send signal that the pot is in fact
    empty. Otherwise they take food from the pot until there's
    nothing left.
    """
    sleep(randint(1, 100) / 100)
    while True:
        shared.mutex.lock()
        if shared.servings == 0:
            print(f'savage {i}: empty pot, waking ALL cooks up')
            shared.empty_pot.signal()
            shared.full_pot.wait()
        print(f'savage {i} takes from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        eat(i)


def cook(i, shared):
    """
    Function for cooks, if they get waken up (if they receive the signal)
    that the pot is empty, all cooks start cooking together. When all of
    them finish cooking, the last cook let's the savages know that N number
    of portions is served, and that they can start eating.
    """
    while True:
        shared.empty_pot.wait()
        print(f'The cook {i} is cooking')
        sleep(randint(50, 200) / 100)
        print(f'The cook {i} finished cooking his part')
        shared.cooks_finished += 1
        shared.barrier.wait()
        shared.mutex_cook.lock()
        if shared.cooks_finished == C:
            print(f'All cooks finished cooking: {M} servings --> pot')
            shared.servings += M
            shared.cooks_finished = 0
            print(f'Cook {i} is letting savages know that the pot is full')
            shared.full_pot.signal()
            shared.empty_pot.clear()
        shared.mutex_cook.unlock()


def main():
    shared = Shared(0)
    savages = []
    cooks = []

    for i in range(N):
        savages.append(Thread(savage, i, shared))

    for i in range(C):
        cooks.append(Thread(cook, i, shared))

    for t in savages + cooks:
        t.join()

if __name__ == "__main__":
    main()
