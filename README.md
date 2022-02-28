# PPDS 2022 - Lab exercises 2

In this lab exercise we try to utilize events and semaphors in parallel programming.

## Contents
- 02_barriers.py
- 02_fibonacci.py

## First & second lab exercise

First and second lab exercises were both implemented in the file 02_barriers.py. 
We primarily aim to understand how barriers work. After understanding how barriers work, we needed to distinguish the difference between events and semaphors. After understanding that semaphors unblock one thread out of N that are waiting by calling signal, while events unblock all threads by calling signal, we tried several experiments.

Using code from seminar that happened on 23.02.2022, we practically had a solid skeleton program that was utilizing semaphors to make barriers. Since we already understood the difference between events and semaphors, changing the functionality was simple.

The one tricky part was to figure out where to put .clear(), to clear all our barrier to be able to reuse them. This was not necessary while using semaphors. I figured this out by simply running the for cycle twice:

```sh
threads = [Thread(barrier_example, sb1, i) for i in range(5)]
[t.join() for t in threads]
print("Round two:")
threads = [Thread(barrier_example, sb1, i) for i in range(5)]
[t.join() for t in threads]
```

The first one ran just fine, but when running the second one, even though the function used was exactly the same, the barriers didn't seem to work. 
This was the part we needed to implement for lab exercise 2. Logically, we want to clear barriers once they finish with their duty, which was in our case in function barrier_example (for exercise 2 where we utilize barrier reusing it was in function barrier_cycle). We added barrier clearing at the very end of our functions, which as expected, seemed to clear the barriers properly and allow us to reuse them multiple times.


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
