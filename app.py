from flask import *
import indicoio
import os
import requests
import json
import pytumblr
from TwitterAPI import TwitterAPI
from instagram.client import InstagramAPI
import secrets

twitter_api=TwitterAPI(secrets.Twitter_consumer,
                        secrets.Twitter_consumer_secret,
                        secrets.Twitter_access_token_key,
                        secrets.Twitter_access_token_secret
                        )


instagram_api=InstagramAPI(client_id=secrets.Instagram_client_id, client_secret=secrets.Instagram_client_secret)

tumblr_client=pytumblr.TumblrRestClient(secrets.Tumblr_consumer,
                                        secrets.Tumblr_consumer_secret,
                                        secrets.Tumblr_oauth_token,
                                        secrets.Tumblr_oauth_token_secret
                                        )
app = Flask(__name__)

@app.route('/')
def home():
    with open('mobidick.txt','r') as f:
        buff = f.read
    return render_template('index.html', buff=buff)

@app.route('/generate', methods='post')
def grabinfo():
    handle = request.form['twitter']
    BigBoom(twitter, fbUname, fbPass, )
    return render_template('results',)


def BigBoom(twitterUname, fbUname, fbPass, ):
    # buffer of aggregate data to be processed.
    aggregate = ""

    # grab tweets for any given area
    r = twitter_api.request('search/tweets', {'q':'pizza', 'locations':'-74,40,-73,41'})
    for item in r:
        aggregate += item['text']
        aggregate += "\n"
        print item['text']

    # grab instagram content
    r = instagram_api.media_search(q='pizza',lat="37.7808851",lng="-122.3948632",distance=1000)
    photos = [ ]
    for media in r:
        photos.append('<img src="%s"/>' % media.get_standard_resolution_url())

    print r
    print ''.join(photos)

    # purge non ASCII characters
    aggregate = ''.join([i if ord(i) < 128 else ' ' for i in aggregate])

app.run(debug=True)
