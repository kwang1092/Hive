#import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
          import Features, KeywordsOptions, SentimentOptions, EntitiesOptions
          
natural_language_understanding = NaturalLanguageUnderstandingV1(
        username='da4002b9-6066-409d-bbaa-85ae5b20a6d5',
        password='yYoaguqXz2w0',
        version='2018-03-16')

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'ZM68mCrT2PNw3yaStE2It0kuk'
consumer_secret = 'Wqz15tXVAm4onbIp4pF3HbRXrUWt3hMF7MxeM6VtU0QEIJDc91'
access_token = '968336866520059904-E0MdLmQvKpP8x6jIw5DJGq1gpuinVYC'
access_token_secret = 'QWcvfx4DcBqHgpyahKeSVl29BaD4j4nZtE3HTOWIr8f0a'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search(q='Bitcoin', lang='en', rpp=20)

for tweet in public_tweets:
    response = natural_language_understanding.analyze(
            text=tweet.text, 
            features=Features(
                sentiment=SentimentOptions())).get_result()
    print(json.dumps(response))
