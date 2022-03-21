# PPDS 2022 - Lab exercises 5

In this exercise we try to implement savages #2 example.

## Contents
- 05_savages.py

## Introduction
In this exercise we try to adjust the savages #1 example, so that instead of 1 cook preparing all the portions, we'd have multiple cooks working together on making a feast.

## Analysis

We start by having a savage walk into the diner. Once he notices there is no food in the pot, he wakes up all the cooks and makes them cook up a feast. Since we want all cooks to cook, we used Event in this example, instead of Semaphor. Once all cooks finish cooking their part, the last one to finish notifies the savages that pot is full and that M number of portions is prepared. We used Barrier here to ensure that ALL cooks would cook exactly once, instead of having one cook possibly cook multiple times due to another cook taking more time. Savages then eat food, similarly to savages #1 example, until the pot is empty, and then they wake up cooks again...

## Pseudocode
```sh
// N = number of savages, M = number of portions, C = number of cooks
N = 3
M = 5
C = 4

// Barrier used to ensure that each cook cooks exactly once 
class SimpleBarrier(object):
    def __init__(self, N):
        self.N = N
        self.cnt = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)
    // Used for cooks to wait for each other to finish cooking
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
    def __init__(self, m):
        self.mutex = Mutex()
        self.mutex_cook = Mutex()
        self.servings = m
        self.full_pot = Semaphore(0)
        // Event that signalizes that the pot is empty. We use Event instead of Semaphore because we want 
        // all of the cooks to begin cooking
        self.empty_pot = Event()
        self.cooks_finished = 0
        self.barrier = SimpleBarrier(C)

// Function used to show that savages are eating in console log
def eat(i):
    print(f'savage {i} is eating')
    sleep(randint(50, 200) / 100)

// Function to simulate savages accessing the pot, notifying cooks that it is empty, eating
def savage(i, shared):
    sleep(randint(1, 100) / 100)
    while True:
        shared.mutex.lock()
        // If the pot is empty, notify the cooks (wake them up)
        if shared.servings == 0:
            print(f'savage {i}: empty pot, waking ALL cooks up')
            // Send the signal that the pot is empty
            shared.empty_pot.signal()
            // Wait until you receive the signal that pot is full again
            shared.full_pot.wait()
        print(f'savage {i} takes from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        eat(i)

// Function used to simulate the cooking of food and notifying the savages that food is ready
def cook(i, shared):
    while True:
        // Wait for signal from savages (no need to cook if there is no savages to eat food)
        shared.empty_pot.wait()
        print(f'The cook {i} is cooking')
        sleep(randint(50, 200) / 100)
        print(f'The cook {i} finished cooking his part')
        shared.cooks_finished += 1
        // Wait for all the cooks to finish cooking
        shared.barrier.wait()
        shared.mutex_cook.lock()
        // Once all cooks finish cooking, fill the pot, and the last cook to finish will notify the savages.
        if shared.cooks_finished == C:
            print(f'All cooks finished cooking: {M} servings --> pot')
            shared.servings += M
            shared.cooks_finished = 0
            print(f'Cook {i} is letting savages know that the pot is full')
            shared.full_pot.signal()
            shared.empty_pot.clear()
        shared.mutex_cook.unlock()
```

## Output

In this example we use 3 savages, 5 portions and 4 cooks.

![Imgur Image](https://i.imgur.com/mZ5p7ZS.png)



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
