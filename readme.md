# Societal Clustering

## before you read anything, know that this won't be done for a little while.


This is an app that will attempt to algorithmically generate personalities using social media aggregation and social analytics.

With the probabilities we derive from the content of social media networks like Instagram, Twitter, and Tumblr, we can use the data as a sample set for a particular region and determine what the average person is like in any given location based on particular interests.

We can aggregate location specific data for any given area and derive a large sample size of people in that area through multiple social networks. We of course also grab an aggregate of data that contains the images people post on tumblr and instagram and analyze them using image processing. Once we have this information we can have a very good sample size of the diversity of any given area.

So we have coverage all text, and photos ever to be posted unto the internet.  

The IBM Watson [Personality Insights][service_url] service uses linguistic analysis to extract cognitive and social characteristics from input text such as email, text messages, tweets, forum posts, and more. By deriving cognitive and social preferences, the service helps users to understand, connect to, and communicate with other people on a more personalized level.

Our Image processing also comes conveniently from Watson's [Visual Recognition](https://github.com/watson-developer-cloud/visual-recognition-nodejs) service. This will get us the most statistically likely string that is inside of the photo.  

So we can give our data aggregate to Watson and hopefully find some useful information about the contents.

## The Goal
  If we aggregate this data we have statistical analysis of the average personality of someone in any of these particular areas. With statistics for reactions based on any given emotions, and the ability to "understand" whether a word is positive or negative, we can eventually come up with statistical models for the most likely reactions to certain events.

  For example if we're given a photo, or a string of text, we can process the photo or video and calculate the most likely response from a person in that area.

  We can algorithmically generate *personalities*. And create a framework of location analysis.

  In Other words we now have the most likely type or person to be in any given area. We can compare cities, people, target our advertisements more efficiently and eventually create programs that completely mirror target markets to automate the process of polling for popularity and simply calculate it. The possibilities are effectively limitless.

## Under the Hood

  The app is using python for it's backend and using various social network API's to grab its information
    It's using [pytumblr](https://github.com/tumblr/pytumblr), [python instagram](https://github.com/Instagram/python-instagram) and of course, [twitterAPI](https://github.com/geduldig/TwitterAPI).
    In addition, the image processing is done by watson's

## Running locally

1. Install [Python 2.7.9 or later](https://www.python.org/downloads/)

2. Copy all of your credentials into a file called `secrets.py`

3. Go to the project folder in a terminal and run: `pip install -r requirements.txt`

4. Start the application `python app.py`

5. Go to `http://localhost:3000`


## Troubleshooting

If you get an error of a module not being defined during the Instagram import call, try this.
```
sudo pip install --upgrade six
```
