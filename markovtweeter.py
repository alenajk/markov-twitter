import os
import twitter
import sys
from markov_oo import TweetableMarkovGenerator

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

#Print info about credentials to make sure they're correct
print api.VerifyCredentials()

tweet = TweetableMarkovGenerator()
source_string = tweet.read_files(sys.argv[1:])
source_chains = tweet.make_chains(source_string)

# Send a tweet
status = api.PostUpdate(tweet.make_text())
print status.text