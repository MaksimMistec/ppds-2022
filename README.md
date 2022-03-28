# PPDS 2022 - Lab exercises 6

In this exercise we try to implement the barber shop example.

## Contents
- 06_barber.py

## Analysis
There is N customers, S seats available and 1 barber. Customers walk into the shop 1 by 1 taking up seats until the barber shop is full, after that, they walk away and try again later. Barber waits for a customer before he starts cutting their hair. He cuts until customer is satisfied (until they send a signal) and then he stops (sends a signal), then both finish and the customer leaves, then next one comes in and the next customer in queue gets their hair cut...

## Output

In this example we use 5 maximum seats in the barber shop (S = 5), and 8 total customers (N = 8). We can see that at no point was there more than 5 people in the barber shop, and that barber is maintaining the proper order of cutting the right people according to the queue.

![Imgur Image](https://i.imgur.com/AxlWK1K.png)



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
