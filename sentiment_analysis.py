import requests


def get_sentiments(tweet_list):
	
	payload = []
	for tweet in tweet_list:
		insert_dict = {"text":tweet.text,"id":tweet.id}
		payload.append(insert_dict)
	
	r = requests.post('http://www.sentiment140.com/api/bulkClassifyJson', data = {'data':payload})
	response = r.json()
	print response