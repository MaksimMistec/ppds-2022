# PPDS 2022 - Lab exercises 3

In this lab exercise we try to experiment in the producer-consumer example shown during lab.

## Contents
- 03_pk.py

## Introduction
We will be using a shared class which will primarily serve as a container. The idea is that, one side, the producer will be producting imaginary packages, and the other side, the consumer will be picking up, or consuming said packages. The idea of this lab is to play around with the numbers such as number of producers, number of consumers, container size and others, and compare how the changes affect the results.

Personally, I analyzed and compared the results by printing out data and comparing them, because I failed to properly draw a 3D graph.

The experiment was conducted by using various combinations of number of producers and producing time, or number of producers and number of consumers. After running the for cycles, the idea was to draw out the graph (which failed) to get even better understanding of how these changes affect our results and possibly how.

## Increasing number of producers
Logically, increasing number of producers increased the production rate, but only so much - because it was still bottlenecked by production speed. At some point, by having too many producers but having too little consumers (!!), the production rate stopped increasing. 

## Increasing number of producers and production time
Much like the previous example, by increasing both producers and lowering the production time (thus making it faster), we simply increase the speed of production up until the point where out container hits the upper limit, then production rate stops increasing.

## Increasing number of consumers (using constant number of producers)
After realising that we are possibly being bottlenecked by number of consumers being too low, we set the consumers to scale from 2 to 10, to see if the production rate will be the same, or if consumers don't really affect the speed of production. (we used 10 producers in this example). 

The results were as expected (and as we have seen in the lab example earlier last week). By using the same amount of producers, but only increasing consumers, we still increased the producing rate, because at first, we would have too little consumers which would result in our container to be constantly full and producers would have to stop producing, but once we had more consumers, the producers could keep producing for longer time, resulting in a higher production rate.



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
