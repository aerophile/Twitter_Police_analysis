import tweepy
import parameters
import process_tweets

auth = tweepy.OAuthHandler(parameters.consumer_key, parameters.consumer_secret)
auth.set_access_token(parameters.access_token, parameters.access_token_secret)

api = tweepy.API(auth)

tweet_collection = []

def obtain_tweets():
	"downloads tweets and removes retweets till required number of tweets are collected"
	reached_end = False
	downloaded_tweets = api.user_timeline(screen_name="DelhiPolice",count = 200,include_rts=False)
	max_id_value = downloaded_tweets[-1].id
	downloaded_tweets = remove_replys(downloaded_tweets)

	while (len(tweet_collection) < parameters.tweets_quantity and reached_end != True):
		
		tweet_collection.extend(downloaded_tweets)
		try:
			downloaded_tweets = api.user_timeline(screen_name="DelhiPolice",count = 200, max_id = max_id_value, include_rts=False)
			max_id_value = downloaded_tweets[-1].id
			downloaded_tweets = remove_replys(downloaded_tweets)
		except:
			reached_end = True

def print_tweet_text(tweet_list):
	i = 1
	for tweet in tweet_list:
		print str(i)+" ",(tweet.text).encode('utf-8')
		i += 1

def remove_replys(tweet_list):
	new_tweet_list = []
	for tweet in tweet_list:
		if tweet.text[0] != '@' or tweet.in_reply_to_status_id is None:
			#print tweet.in_reply_to_status_id, tweet.text
			new_tweet_list.append(tweet)
	return new_tweet_list

obtain_tweets()
print_tweet_text(tweet_collection)
print process_tweets.determine_post_type(tweet_collection)
		
