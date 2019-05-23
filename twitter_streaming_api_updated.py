print('Twitter Streaming API')
# https://github.com/skathirmani/text-analytics
# Click twitter_streaming_api.py -> Click Raw -> Copy the code -> Paste it here

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import glob
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

senti = SentimentIntensityAnalyzer()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


class StdOutListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        print('----Some one tweeted about Elections 2019 ----')
        curr_tweet = {
            'text': data['text'],
            'created_at': data['created_at'],
            'user_name': data['user']['name'],
            'user_location': data['user']['location'],
            'souce': data['source'],
            'compound': senti.polarity_scores(data['text'])['compound'],
        }
        print(curr_tweet['text'])
        print('Positive' if curr_tweet['compound'] > 0 else 'Negative')
        
        series_tweet = pd.Series(curr_tweet)
        
        file_name = 'elections_tweet.csv'
        try:
            if file_name in glob.glob('*.csv'):
                # Append the result
                with open(file_name, 'a') as f:
                    series_tweet.to_csv(f, index=False, header=False)
            else:
                # Create a file and append the result
                    series_tweet.to_csv(file_name, index=False)
        except UnicodeEncodeError:
            pass
            
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['#ElectionResults2019'])
    
    
    
    
    
    
    