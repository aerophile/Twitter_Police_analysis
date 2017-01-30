from afinn import Afinn
afinn = Afinn()

def get_sentiments(tweet_list):
	
	sentiment_results=[]
	for tweet in tweet_list:
		sentiment_results.append(afinn.score((tweet.text).encode('utf-8')))

	return sentiment_results