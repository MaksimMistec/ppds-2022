#####################################################################
#
# File name: 04_powerstation.py
# Author: Maksim Mištec
# Creation date: 03/14/2022
# License: MIT
# Purpose: exercise showing the parallel execution of sensors
# and monitors monitoring the sensors. The monitors have to wait
# before all the sensors write something before they can read it.
#
#####################################################################
from fei.ppds import Mutex, Semaphore, Thread, Event, print
from time import sleep
from random import randint


class Lightswitch:
    """
    Class we use to primarily lock/unlock monitors and sensors
    """
    def __init__(self):
        self.mutex = Mutex()
        self.counter = 0

    def lock(self, sem):
        self.mutex.lock()
        counter = self.counter
        self.counter += 1
        if self.counter == 1:
            sem.wait()
        self.mutex.unlock()
        return counter

    def unlock(self, sem):
        self.mutex.lock()
        self.counter -= 1
        if self.counter == 0:
            sem.signal()
        self.mutex.unlock()


def init():
    """
    Main function. Used to initialize all necessary tools and
    get the threads running.
    """
    access_data = Semaphore(1)
    semaphore = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    valid_data = Event()

    for monitor_id in range(8):
        Thread(monitor, monitor_id, valid_data, semaphore, ls_monitor,
               access_data)

    for sensor_id in range(3):
        Thread(sensor, sensor_id, semaphore, ls_sensor, valid_data, access_data)


def monitor(monitor_id, valid_data, semaphore, ls_monitor, access_data):
    """
    Function used to manage monitors. They wait until all sensors write
    their part once before they can start monitoring.
    """
    valid_data.wait()

    while True:
        reading_length = randint(40, 50) / 1000
        sleep(reading_length)
        semaphore.wait()
        number_of_reading_monitors = ls_monitor.lock(access_data)
        semaphore.signal()

        print(f'monit "{monitor_id:02d}": '
              f'number_of_reading_monitors={number_of_reading_monitors:02d},'
              f'reading_length={reading_length:5.3f}')
        ls_monitor.unlock(access_data)


def sensor(sensor_id, semaphore, ls_sensor, valid_data, access_data):
    """
    Function used to write imaginary data that monitors will then read.
    """
    while True:
        sleep(randint(50, 60)/1000)
        semaphore.wait()
        semaphore.signal()

        number_of_writing_sensors = ls_sensor.lock(access_data)
        if sensor_id == 2:
            writing_length = randint(20, 25) / 1000
        else:
            writing_length = randint(10, 20) / 1000
        print(f'sensor "{sensor_id:02d}":  '
              f'number_of_writing_sensors={number_of_writing_sensors:02d}, '
              f'writing_length={writing_length:5.3f}')
        sleep(writing_length)
        valid_data.signal()
        ls_sensor.unlock(access_data)


if __name__ == '__main__':
    init()
