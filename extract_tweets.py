import tweepy
import parameters
import process_tweets

auth = tweepy.OAuthHandler(parameters.consumer_key, parameters.consumer_secret)
auth.set_access_token(parameters.access_token, parameters.access_token_secret)

api = tweepy.API(auth)

tweet_collection = []

def obtain_tweets():
	"downloads tweets and removes retweets till required number of tweets are collected"
	downloaded_tweets = api.user_timeline(screen_name="DelhiPolice",count = 200,include_rts=False)
	max_id_value = downloaded_tweets[-1].id

	while (len(tweet_collection) < parameters.tweets_quantity):
		
		tweet_collection.extend(downloaded_tweets)
		downloaded_tweets = api.user_timeline(screen_name="DelhiPolice",count = 200, max_id = max_id_value, include_rts=False)
		max_id_value = downloaded_tweets[-1].id
		

def print_tweet_text(tweet_list):
	i = 1
	for tweet in tweet_list:
		print str(i)+" ",(tweet.text).encode('utf-8')
		i += 1



obtain_tweets()
#print_tweet_text(tweet_collection)
print process_tweets.calculate_popular_hashtags(tweet_collection)
		
