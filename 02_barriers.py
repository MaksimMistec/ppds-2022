from random import randint
from time import sleep
from fei.ppds import Thread, Mutex, Event, print


class SimpleBarrier:
    def __init__(self, n):
        self.n = n
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.n:
            self.counter = 0
            # if we reach this point, all barriers will get unblocked
            self.event.signal()
        self.mutex.unlock()
        # the first n-1 barriers will freeze and wait until the last barrier
        # after that, all barriers will get unblocked with signal()
        self.event.wait()


def barrier_example(barrier, thread_id):
    """
    Function used to test barrier functionality
    First, all threads send their first message
    Then, threads wait until the last thread finishes
    sending the first message
    Then, barriers unblock and all threads send
    their second message
    """
    sleep(randint(1, 10)/10)
    print("thread %d before barrier" % thread_id)
    barrier.wait()
    print("thread %d after barrier" % thread_id)
    # zeroing out all the settings from previous use
    # which allows us to reuse the same barrier
    barrier.event.clear()


def before_barrier(thread_id):
    """
    Simple function that prints out a message for each barrier
    Used for visual testing, to see if barriers work as expected.
    """
    sleep(randint(1, 10)/10)
    print(f"BEFORE barrier {thread_id}")


def after_barrier(thread_id):
    """
    Simple function that prints out a message for each barrier
    Used for visual testing, to see if barriers work as expected.
    """
    print(f"AFTER barrier {thread_id}")
    sleep(randint(1, 10)/10)


def barrier_cycle(b1, b2, thread_id):
    """
    Function that runs cycles using barriers
    Used to test barrier reusability
    """
    for i in range(10):
        before_barrier(thread_id)
        b1.wait()
        after_barrier(thread_id)
        b2.wait()
        # crucial part!! if we don't clear our barriers
        # they will not be reusable again in the next cycle
        b1.event.clear()
        b2.event.clear()

sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)

# lab exercise 1
# doing 2 for cycles to check if releasing barrier works as intended
# purposely leaving the following commented code here as it helped me
# figure out where to release barriers (more in documentation)

# threads = [Thread(barrier_example, sb1, i) for i in range(5)]
# [t.join() for t in threads]
# print("Round two:")
# threads = [Thread(barrier_example, sb1, i) for i in range(5)]
# [t.join() for t in threads]

threads = [Thread(barrier_cycle, sb1, sb2, i) for i in range(5)]
[t.join() for t in threads]
