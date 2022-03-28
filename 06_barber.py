#####################################################################
#
# File name: 06_barber.py
# Author: Bc. Maksim Mištec
# Creation date: 3/28/2022
# License: MIT
# Purpose: Barber shop example, where customers try to enter barber
# shop until it's full, after that, they turn around and try again
# later. Barber doesn't start working until there's a customer
#
######################################################################
from fei.ppds import Thread, Mutex, Semaphore, print
from random import randint
from time import sleep


"""
N - number of customers
S - number of seats at barber shop
"""
N = 8
S = 5


class Shared():
    """
    Shared class we use for both barber and customers.
    """
    def __init__(self):
        # first 2 semaphores are used to signal customer/barber
        # at the same time to start cutting/getting hair cut.
        # second 2 are used to signal that they're both finished.
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        self.customerDone = Semaphore(0)
        self.barberDone = Semaphore(0)
        # first mutex used during hair cutting (only 1 customer can
        # have their hair cut at the same time)
        # second one is used to simulate customers entering shop 1 by 1
        self.mutex_haircut = Mutex()
        self.mutex = Mutex()
        self.takenSeats = 0
        self.totalSeats = S
        self.queue = []

    def enter(self, customer_id):
        """
        Function that checks if the barber shop is full, if not,
        add the customer to the queue. If yes, they turn around and leave
        """
        if self.takenSeats < self.totalSeats:
            self.mutex.lock()
            print(f'Customer {customer_id} has ENTERED the barber shop..')
            self.queue.append(customer_id)
            if self.takenSeats == 0:
                print(f'Customer {customer_id} is WAKING barber up!!')
            self.takenSeats += 1
            self.mutex.unlock()
        if self.takenSeats == self.totalSeats:
            print(f'Customer {customer_id} CAN NOT ENTER because its full')


def customer(customer_id, shared):
    """
    Customer function. Simulates entering the shop. If customer is not
    in queue (means that shop was full when he tried), break out of
    while loop. Otherwise, simulate customer getting their hair
    cut and leave shop as explained in the seminar.
    """
    while True:
        sleep(randint(200, 500) / 100)
        shared.enter(customer_id)

        if customer_id not in shared.queue:
            continue

        shared.mutex_haircut.lock()
        shared.customer.signal()
        shared.barber.wait()

        print(f'Customer {customer_id} is GETTING a haircut..')
        sleep(randint(1, 100) / 100)

        shared.customerDone.signal()
        print(f'Customer {customer_id} is DONE getting a harcut.')
        shared.barberDone.wait()
        shared.mutex_haircut.unlock()

        shared.mutex.lock()
        print(f'Customer {customer_id} is LEAVING the barber shop..')
        shared.takenSeats -= 1
        shared.queue.pop(0)
        shared.mutex.unlock()


def barber(shared):
    """
    Barber function. Barber first waits for a customer to show up
    before he starts working (you could say he's asleep). After signals
    that he's ready and starts cutting hair. Cuts hair until customer is
    satisfied with the cut and sends a signal that he's finished at
    the end.
    """
    while True:
        shared.customer.wait()
        shared.barber.signal()
        print(f'Barber is cutting hair..')
        sleep(randint(1, 100) / 100)
        shared.customerDone.wait()
        shared.barberDone.signal()
        print(f'Barber finished cutting hair..')


def main():
    shared = Shared()
    customers = []

    for i in range(N):
        customers.append(Thread(customer, i, shared))

    barber_work = Thread(barber, shared)

    for t in customers:
        t.join()

    barber_work.join()


if __name__ == "__main__":
    main()
