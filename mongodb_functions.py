import pymongo


# some of this code orginates from http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/


def create_dict(tweet):

    data ={}
    data['created_at'] = tweet.created_at
    data['geo'] = tweet.geo
    data['id'] = tweet.id
    data['in_reply_to_status_id'] = tweet.in_reply_to_status_id
    data['text'] = tweet.text
    data['entities'] = tweet.entities
    data['hashtags'] = tweet.entities["hashtags"]
    return data


def insert_tweet(db_name,collection_name,tweet_list):
	try:
		conn=pymongo.MongoClient()
		print "Connected successfully!!!"	

		db = conn[db_name]
		collection_obj = db[collection_name]
		#process tweet and insert
		for tweet in tweet_list:
			collection_obj.insert(create_dict(tweet))
	
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e




