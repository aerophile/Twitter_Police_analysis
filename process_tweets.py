import collections
import sentiment_analysis_afinn
import mongodb_functions

def calculate_tweet_frequency(tweet_list):
	"returns a tweet frequency and list of frequencies based on calculations from all obtained tweets"
	time_differences = []
	tweet_frequency_list=[]
	for i in range(0,len(tweet_list)-1):
		timedelta_seconds = (tweet_list[i].created_at - tweet_list[i+1].created_at).total_seconds()
		time_differences.append( timedelta_seconds )
		

	avg_timeperiod = sum(time_differences)/len(time_differences)

	avg_tweets_persecond = 1/avg_timeperiod

	avg_tweets_perday = avg_tweets_persecond * 60 * 60 * 24

	for time_difference  in time_differences:
		try:
			freq = round(((1/time_difference)* 60 * 60 * 24),2)
			tweet_frequency_list.append(freq)
		except:
			continue

	avg_tweets_perday = round(avg_tweets_perday,2)

	return avg_tweets_perday,tweet_frequency_list

def calculate_popular_hashtags(tweet_list):
	"returns the ten most popular hastags as a list of tupples with each tupple containing the zeroth index as hashtag and first index as occurance frequency"
	hashtags_list = []
	for tweet in tweet_list:
		for hashtag in tweet.entities["hashtags"]:
			hashtags_list.append(hashtag["text"])
		
	popular_hashtags_dictionary = collections.Counter(hashtags_list)
	popular_hashtags = popular_hashtags_dictionary.most_common(10)
	#print popular_hashtags
	return popular_hashtags



def determine_post_type(tweet_list):
	"returns engagement stats for posts having images only/text only/both"
	image_only = 0
	text_only = 0
	image_and_text = 0
	likes = [0,0,0]
	retweets = [0,0,0]
	for tweet in tweet_list:
		try:
			if tweet.entities["media"][0]["type"] == "photo" :
				if tweet.text[0:13] == 'https://t.co/' and len(tweet.text) == 23: 
					#Image only condition
					# Only picture tweets have the text as image link of lenth 23
					image_only += 1
					likes[0] += tweet.favorite_count
					retweets[0] += tweet.retweet_count
				else:
					# Likely to be image and text
					image_and_text += 1
					likes[2] += tweet.favorite_count
					retweets[2] += tweet.retweet_count
			
		except:
			text_only += 1
			likes[1] += tweet.favorite_count
			retweets[1] += tweet.retweet_count
	
	return_list = [{"image_only":[image_only,int(likes[0]),int(retweets[0])," Image only Posts"]},
					{"text_only":[text_only,int(likes[1]),int(retweets[1]),"Text posts"]},
					{"images_and_text":[image_and_text,int(likes[2]),int(retweets[2]),"Image and Text Posts"]}
					]					
	return return_list


def process_tweets_function(tweet_list,screen_name):
	tweet_frequency,tweet_frequency_list = calculate_tweet_frequency(tweet_list)
	popular_hashtags = calculate_popular_hashtags(tweet_list)
	post_type_count = determine_post_type(tweet_list)
	sentiment_result_list = sentiment_analysis_afinn.get_sentiments(tweet_list)
	try:
		mongodb_functions.insert_tweet("police_analysis",screen_name,tweet_list)
	except:
		print "mongodb_error"

	return_obj = {"tweet_frequency": [tweet_frequency,tweet_frequency_list,len(tweet_frequency_list)],
					"popular_hastags": popular_hashtags,
					"post_type_count": post_type_count,
					" sentiment_result_list" : sentiment_result_list}
	return return_obj

	
