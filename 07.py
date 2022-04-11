#####################################################################
#
# File name: 07.py
# Author: Bc. Maksim Mištec
# Creation date: 4/11/2022
# License: MIT
# Purpose: Example that alternates 2 programs using a scheduler
#
# Inspiration: https://www.dabeaz.com/coroutines/Coroutines.pdf
#
######################################################################
from random import randint
from fei.ppds import print


class Scheduler():
    """
    Scheduler class used to add programs to the queue,
    then pop them (FIFO) in order that they were added.
    When exception StopIteration is called, close the
    remaining tasks.
    """
    def __init__(self):
        self.tasks = []

    def schedule(self, task):
        next(task)
        self.tasks.append(task)

    def start(self):
        value = 0
        while True:
            try:
                task = self.tasks.pop(0)
                value = task.send(value)
                self.tasks.append(task)
            except StopIteration:
                for i in self.tasks:
                    i.close()
                break


def subtract(starting_number, ending_number):
    """
    First of the two programs, simply substracts numbers
    until a certain limit is reached, after that breaks.
    """
    count = 0
    total = starting_number
    sub_number = 0
    while True:
        total -= sub_number
        yield total
        if total < ending_number:
            print(f'Finished because {total} is lower than {ending_number}')
            break
        sub_number = randint(1, 5)
        print(f'Subtracting {sub_number} from {total}')


def odd_number():
    """
    Second of the two programs, receives value through
    yield and checks if it's an even number and prints it out.
    """
    count = 0
    total = 0
    while True:
        n = yield total
        if n % 2 == 0:
            print(f'Number {n} is even')
            count += 1
        else:
            print(f'Number {n} is not even')


def main():
    gen = Scheduler()
    gen.schedule(subtract(30, 10))
    gen.schedule(odd_number())
    gen.start()


if __name__ == "__main__":
    main()