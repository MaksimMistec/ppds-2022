# PPDS 2022 - Lab exercises 8

In this exercise we try to implement two examples, one of synchronous http request and one of asynchronous http request and compare the results.

## Contents
- 08_sync.py
- 08_async.py

## Introduction
These 2 programs pull json data from https://pokeapi.co/. 
We simply print out N number of pokemon names in this program.

## Synchronous
Simple program that pulls json data from the previously mentioned server and prints them out. In this example we use the requests library to make HTTP requests. At the end prints out how much time elapsed since the beginning of the program. In this example we print 20 pokemons (also in async version).

![Imgur Image](https://i.imgur.com/2dZW1Wj.png)

## Asynchronous
Simple program that like sync version pulls json data from the pokemon server and prints 20 pokemons out. In this example we use aiohttp library to make HTTP requests. The differences from the sync version are:
1. Function that pulls json data is changed to async because it is used to get data from the server, which also means we will have to wait a certain time between getting data.
2. Function that pulls json data also has await in it. The await keyword passes control back to the event loop, suspending the execution of the surounding coroutine and letting the event loop run other things until the result that is being awaited is returned
3. Added async to main function because it serves as a scheduler

![Imgur Image](https://i.imgur.com/nNbwasr.png)

## Sync vs async comparison
We can see that in this example async performs much better, especially in the speed department(2.5107s vs 0.2550s).
Obviously as you can see, using different libraries like aiohttp to make HTTP requests can result in a big performance boost to code and save a lot of time when making large amount of requests.

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
