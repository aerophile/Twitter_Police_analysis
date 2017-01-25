import tweepy
import parameters

auth = tweepy.OAuthHandler(parameters.consumer_key, parameters.consumer_secret)
auth.set_access_token(parameters.access_token, parameters.access_token_secret)

api = tweepy.API(auth)

tweet_collection = []

def obtain_tweets():
	"downloads tweets and removes retweets till required number of tweets are collected"
	downloaded_tweets = api.user_timeline(screen_name="BlrCityPolice",count = 200,include_rts=False)
	max_id_value = downloaded_tweets[-1].id

	while (len(tweet_collection) < parameters.tweets_quantity):
		
		tweet_collection.extend(downloaded_tweets)
		downloaded_tweets = api.user_timeline(screen_name="BlrCityPolice",count = 200, max_id = max_id_value, include_rts=False)
		max_id_value = downloaded_tweets[-1].id
		

def print_tweet_text(tweet_list):
	i = 1
	for tweet in tweet_list:
		print str(i)+" ",tweet.text
		i += 1

def process_tweets(tweet_list):
	tweet_frequency = calculate_tweet_frequency(tweet_list)


obtain_tweets()
print_tweet_text(tweet_collection)

		
