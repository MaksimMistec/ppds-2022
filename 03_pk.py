from fei.ppds import Mutex, Semaphore, Thread
from fei.ppds import print
from random import randint
from time import sleep
import matplotlib.pyplot as plt


class Shared(object):
    """
    Class we use to do internal counting of how many
    "packages" are being produced.
    """
    def __init__(self, N):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(N)
        self.items = Semaphore(0)
        self.count = 0


def producer(shared, timer):
    """
    Function that manages producer side.
    Waits for shared contained to have a space before
    generating more packages.
    """
    while True:
        shared.free.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        shared.count += 1
        sleep(randint(1, 10)/timer)
        shared.mutex.unlock()
        shared.items.signal()


def consumer(shared):
    """
    Function that manages consumer side.
    Can only take a package if the shared container is not empty.
    """
    while True:
        shared.items.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10)/100)
        shared.mutex.unlock()
        sleep(randint(1, 10)/10)


def main():
    """
    Main function. Used for various experiments,
    mainly comparing how increasing/decreasing
    amount of producers and consumers affects the
    production rate.
    """
    counter = 0
    x = []
    y = []
    z = []
    producers_nr = [2, 4, 6, 8, 10]
    prod_times = [100, 150, 200, 250, 300]
    for k in range(5):
        print(producers_nr[k])
        for j in range(5):
                print(prod_times[j])
                for i in range(5):
                    s = Shared(10)
                    c = [Thread(consumer, s) for _ in range(2)]
                    p = [Thread(producer, s, prod_times[j]) for _ in range(5)]

                    sleep(10/prod_times[j])
                    s.finished = True
                    print(f"final thread {i}: waiting to finish")
                    s.items.signal(100)
                    s.free.signal(100)
                    [t.join() for t in c+p]

                    produced = s.count
                    produced_per_second = produced / (10/prod_times[j])

                    print(f"final thread {i}: finished")
                    print(f"Produced {produced_per_second} in 1 second")
                    print(f"Total count {produced}")

                    x.append(prod_times[j])
                    y.append(5)
                    z.append(produced_per_second)
                    counter += 1
    # fig = plt.figure()
    # ax = plt.axes(projection ='3d')
    # ax.plot(x, y, z)
    # plt.show()

if __name__ == "__main__":
    main()
