# Sentiment-Analysis
Contains Python files to get Twitter, Youtube data and then analyse it.

For getting the tweets, I have used the tweepy library. I am also using various other libraries like csv, requests etc. for storing the tweets in a csv file.

Before clicking on SK_twitter.py file, make sure you have a twitter developer account and the 4 secret keys. Add these 4 keys in a file called auth.k.

If you don't have a twitter developer account and the keys, this is a really easy to follow [tutorial](http://docs.inboundnow.com/guide/create-twitter-application/).

Steps for running the program for twitter:

1) Click on the SK_twitter.py file
2) This will open a web page, enter the topic and the number of tweets (Maximum 1000) you want to get
3) A csv file will be downloaded once you click on the submit button (this will take some time)
4) Open the Jupyter notebook (.ipynb) file and analyse as well as plot the results from tweets

Similary for getting results from Youtube, make sure you have a google developer account and enable the youtube API in the project.

A useful and easy to follow [tutorial](https://www.youtube.com/watch?v=pP4zvduVAqo) for enabling the youtube API for your project. 

Steps for running the program for youtube:

1) Click on the SK_youtube.py file
2) This will open a web page, enter the topic 
3) A csv file will be downloaded once you click on the submit button (this will take some time)
4) Open the Jupyter notebook (.ipynb) file and analyse as well as plot the results from top 25 results from youtube. 
