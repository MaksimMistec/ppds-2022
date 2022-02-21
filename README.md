In this lab exercise we try to create two different examples of how locks can be used in parellel programming.


The skeleton code used in these two examples was taken from the seminar that happened on 16.02.2022.


These solutions were tested in Python versions 3.8 and 3.10.


In the first example (named first.py):
We utilize the lock function in a way, where we lock one thread before the while loop starts, and unlock it after the while loop ends. This results in one thread running the whole loop while the other thread is locked out completely. After the first thread finishes running it's while loop (this means that all elements were incremented by 1 and our counter has reached the end), the second thread starts running it's while loop, however, because the shared counter is already at the point where it's the same or greater than the size of our list, it instantly ends. The expected output should look like this: [(1, 10000000), (0, 10)], the first part being the size of our thread, and the last 10 elements are filled with zeroes, which we used to check if the counter isn't reaching out of bounds and overwriting unwanted data.


In the second example (named second.py):
We utilize the lock function in a different way from the first example. We use the lock function inside the while loop, and the way it should work is that both threads start running at the same time, one of them reaches the lock first, locks the other thread, increments the element by 1, then increments the counter, and then unlocks the other thread. The second thread that was just unlocked will now lock the first thread, do the same process as the first one, then unlock the first thread again. This process will repeat as the two threads alternate until they reach the second last element. Since at this point both threads are already running (one of them is probably locked) we have a situation like this:

t1 is at shared counter 998 (out of 1000 elements as an example)
t2 is at shared counter 998
t1 locks t2, increments the element and the counter, shared counter is now at 999
t2 unlocks, shared couter is at 999
t1 starts new while loop, shared counter 999 
!! At this point we would have a situation where we would reach out of range, so we added an if statement that checks if the counter is at shared.end - 1 position. If yes, it breaks out of the while loop. This would result the t2 thread to finish incrementing it's element and counter to 1000, and t1 stopping before it increments the 1001st element.
Additionally, another if condition is added, that the while loop would only stop if the size of our list is greater than 1 (without this condition, our while loop would never even run on lists with just 1 element). The expected result in this example should be the same as first: [(1, 10000000), (0, 10)]
