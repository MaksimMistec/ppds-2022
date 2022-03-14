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
    turniket = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    valid_data = Event()

    for monitor_id in range(8):
        Thread(monitor, monitor_id, valid_data, turniket, ls_monitor,
               access_data)

    for sensor_id in range(3):
        Thread(sensor, sensor_id, turniket, ls_sensor, valid_data, access_data)


def monitor(monitor_id, valid_data, turniket, ls_monitor, access_data):
    """
    Function used to manage monitors. They wait until all sensors write
    their part once before they can start monitoring.
    """
    valid_data.wait()

    while True:
        reading_length = randint(40, 50) / 1000
        sleep(reading_length)
        turniket.wait()
        pocet_citajucich_monitorov = ls_monitor.lock(access_data)
        turniket.signal()

        print(f'monit "{monitor_id:02d}": '
              f'pocet_citajucich_monitorov={pocet_citajucich_monitorov:02d},'
              f'reading_length={reading_length:5.3f}')
        ls_monitor.unlock(access_data)


def sensor(sensor_id, turniket, ls_sensor, valid_data, access_data):
    """
    Function used to write imaginary data that monitors will then read.
    """
    while True:
        sleep(randint(50, 60)/1000)
        turniket.wait()
        turniket.signal()

        pocet_zapisujucich_cidiel = ls_sensor.lock(access_data)
        if sensor_id == 2:
            trvanie_zapisu = randint(20, 25) / 1000
        else:
            trvanie_zapisu = randint(10, 20) / 1000
        print(f'sensor "{sensor_id:02d}":  '
              f'pocet_zapisujucich_cidiel={pocet_zapisujucich_cidiel:02d}, '
              f'trvanie_zapisu={trvanie_zapisu:5.3f}')
        sleep(trvanie_zapisu)
        valid_data.signal()
        ls_sensor.unlock(access_data)


if __name__ == '__main__':
    init()
