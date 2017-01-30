import extract_tweets
import parameters
import process_tweets as p

for handle in parameters.handles:
	tweet_list = extract_tweets.obtain_tweets(handle)
	extract_tweets.print_tweet_text(tweet_list)
	result = p.process_tweets_function(tweet_list,handle)
	print result

