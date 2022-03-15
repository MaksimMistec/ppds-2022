# PPDS 2022 - Lab exercises 4

In this lab exercise we try to implement nuclear power plant #2 example.

## Contents
- 04_powerstation.py

## Introduction
Using the example from the seminar (nuclear power plant #1 example), we get to practically work with identical module structure. There are only a few differences between these two examples:
1. The number of sensors and monitors are different.
2. Writing data in example #2 doesn't use one writing timer, but instead each sensor has their own different values.
3. Monitors have reading time randomized between 40-50 ms, instead of the previous 500 ms flat.
4. Monitors can start working only when all sensors are done writing.

More info on how it was done in the following pseudocode:

```sh
def init():
    access_data = Semaphore(1)
    semaphore = Semaphore(1)
    ls_monitor = Lightswitch()
    ls_sensor = Lightswitch()
    valid_data = Event()
    for monitor_id in range(8):
        Thread(monitor, monitor_id, valid_data, semaphore, access_data)
    for sensor_id in range(3):
        Thread(sensor, sensor_id, semaphore, ls_sensor, valid_data, access_data)

def monitor(monitor_id, valid_data, semaphore, ls_monitor, access_data):
    // monitor does not work until sensors are done writing
    valid_data.wait()
    
    while True:
        // monitors take 40-50 ms to read data from sensors
        reading_length = randint(40, 50) / 1000
        sleep(reading_length)
        // blocking the semaphore to stop the sensors from writing
        semaphore.wait()
        // getting access to the data storage where sensors were writing
        number_of_reading_monitors = ls_monitor.lock(access_data)
        semaphore.signal()
        // simulating access to the storage by printing it out
        print(f'monit "{monitor_id:02d}":number_of_reading_monitors={number_of_reading_monitors:reading_length={
        reading_length:5.3f}')
        // unlocking the LS and leaving the data storage
        ls_monitor.unlock(access_data)


def sensor(sensor_id, semaphore, ls_sensor, valid_data, access_data):
    while True:
        // sensors take 50-60 ms to initialize
        sleep(randint(50, 60)/1000)
        // sensors run until they are stopped by monitors
        semaphore.wait()
        semaphore.signal()
        // we gain access to the data storage
        number_of_writing_sensors = ls_sensor.lock(access_data)
        // since two of our sensors take the same amount of time to write data, and the last one takes a different
        // amount, we make sure the third sensor always has a different writing length
        if sensor_id == 2:
            writing_length = randint(20, 25) / 1000
        else:
            writing_length = randint(10, 20) / 1000
        // simulating writing to the storage by printing it out
        print(f'sensor "{sensor_id:02d}": number_of_writing_sensors={number_of_writing_sensors:02d}
        writing_length={writing_length:5.3f}')
        sleep(writing_length)
        // we send a signal, signaling that the data written is there and valid
        valid_data.signal()
        // we leave the data storage
        ls_sensor.unlock(access_data)

```
[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
