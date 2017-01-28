import collections

def calculate_tweet_frequency(tweet_list):
	
	time_differences = []
	for i in range(0,len(tweet_list)-1):
		timedelta_seconds = (tweet_list[i].created_at - tweet_list[i+1].created_at).total_seconds()
		time_differences.append( timedelta_seconds )
		

	avg_timeperiod = sum(time_differences)/len(time_differences)

	avg_tweets_persecond = 1/avg_timeperiod

	avg_tweets_perday = avg_tweets_persecond * 60 * 60 * 24

	return avg_tweets_perday

def calculate_popular_hashtags(tweet_list):
	"returns the ten most popular hastags as a list of tupples with each tupple containing the zeroth index as hashtag and first index as occurance frequency"
	hashtags_list = []
	for tweet in tweet_list:
		for hashtag in tweet.entities["hashtags"]:
			hashtags_list.append(hashtag["text"])
		
	popular_hashtags_dictionary = collections.Counter(hashtags_list)
	popular_hashtags = popular_hashtags_dictionary.most_common(10)
	print popular_hashtags



def determine_photos(tweet_list):
	image_only = 0
	text_only = 0
	imag_and_text = 0
	for tweet in tweet_list:
		try:
			if tweet.entities["media"][0]["type"] == "photo" :
				if tweet.text[0:13] == 'https://t.co/' and len(tweet.text) == 23: 
					#Image only condition
					# Only picture tweets have the text as image link of lenth 23
					image_only += 1
				else:
					# Likely to be image and text
					imag_and_text += 1
			
		except:
			text_only += 1
	
	print "image only ", image_only
	print "text only" , text_only
	print "image and text", imag_and_text


def process_tweets(tweet_list):
	tweet_frequency = calculate_tweet_frequency(tweet_list)
