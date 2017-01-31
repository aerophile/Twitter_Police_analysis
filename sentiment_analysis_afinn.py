from afinn import Afinn
afinn = Afinn()

def get_sentiments(tweet_list):
	
	sentiment_results=[]
	negative = 0
	positive = 0
	neutral = 0
	for tweet in tweet_list:
		score = afinn.score((tweet.text).encode('utf-8'))
		if score < 0 :
			negative += (score*-1)
		elif score > 0:
			positive += score
		else :
			neutral += 1
	sum_results = negative + positive + neutral
	negative = round(negative/sum_results,2) * 100
	positive = round(positive/sum_results,2) * 100
	neutral= round(neutral/sum_results,2) * 100

	sentiment_results=[int(negative),int(positive),int(neutral)]

	return sentiment_results