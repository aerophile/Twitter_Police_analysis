from flask import Flask, render_template,url_for
import sys
sys.path.append('../')
from ps17_shubham_gupta.main import *
import threading
import ps17_shubham_gupta.parameters as p
app = Flask(__name__)



def worker():
	print "<<<refresh thread intialized>>>"
	produce_result()
	threading.Timer(3600*12, worker).start()# refresh every 12 hours = 3600*12 seconds
	print "<<<Data refreshed>>>"

@app.route('/')
@app.route('/Bangalore')
def ban():
	city_page = 'Bangalore'	
	result = results[city_page]
	
	labels = [result['popular_hastags'][0][0],result['popular_hastags'][1][0],result['popular_hastags'][2][0],
	result['popular_hastags'][3][0],result['popular_hastags'][4][0],result['popular_hastags'][5][0],
	result['popular_hastags'][6][0],result['popular_hastags'][7][0],result['popular_hastags'][8][0],
	result['popular_hastags'][9][0]]
	values = [result['popular_hastags'][0][1],result['popular_hastags'][1][1],result['popular_hastags'][2][1],
	result['popular_hastags'][3][1],result['popular_hastags'][4][1],result['popular_hastags'][5][1],
	result['popular_hastags'][6][1],result['popular_hastags'][7][1],result['popular_hastags'][8][1],
	result['popular_hastags'][9][1]]
	labels1 = ["Text Likes","Text Retweets","Image and Text likes","Image and Text retweets","Image Likes","Image Retweets"]
	values1 = [result['post_type_count'][1]['text_only'][1],result['post_type_count'][1]['text_only'][2],
	result['post_type_count'][2]['images_and_text'][1],result['post_type_count'][2]['images_and_text'][2],
	result['post_type_count'][0]['image_only'][1],result['post_type_count'][0]['image_only'][2]]
	linechart_x = list(range(result['tweet_frequency'][2]))
	key = ""
	for key,value in p.city.iteritems():
		if value == city_page:
			break

	acc_link = "http://twitter.com/" + key
	max_type = result['post_type_count'][1]['text_only']
	if max_type[0] < result['post_type_count'][2]['images_and_text'][0]:
		max_type = result['post_type_count'][2]['images_and_text']
	if max_type[0] < result['post_type_count'][0]['image_only'][0]:
		max_type = result['post_type_count'][0]['image_only']

	try:
		return render_template("index.html",city=city_page,result = result,acc_link=acc_link,max_type = max_type, values=values, labels=labels,linechart_x=linechart_x, values1=values1, labels1=labels1)
	except Exception, e:
		return str(e)

@app.route('/Mumbai')
def mum():
	city_page = 'Mumbai'	
	result = results[city_page]
	
	labels = [result['popular_hastags'][0][0],result['popular_hastags'][1][0],result['popular_hastags'][2][0],
	result['popular_hastags'][3][0],result['popular_hastags'][4][0],result['popular_hastags'][5][0],
	result['popular_hastags'][6][0],result['popular_hastags'][7][0],result['popular_hastags'][8][0],
	result['popular_hastags'][9][0]]
	values = [result['popular_hastags'][0][1],result['popular_hastags'][1][1],result['popular_hastags'][2][1],
	result['popular_hastags'][3][1],result['popular_hastags'][4][1],result['popular_hastags'][5][1],
	result['popular_hastags'][6][1],result['popular_hastags'][7][1],result['popular_hastags'][8][1],
	result['popular_hastags'][9][1]]
	labels1 = ["Text Likes","Text Retweets","Image and Text likes","Image and Text retweets","Image Likes","Image Retweets"]
	values1 = [result['post_type_count'][1]['text_only'][1],result['post_type_count'][1]['text_only'][2],
	result['post_type_count'][2]['images_and_text'][1],result['post_type_count'][2]['images_and_text'][2],
	result['post_type_count'][0]['image_only'][1],result['post_type_count'][0]['image_only'][2]]
	linechart_x = list(range(result['tweet_frequency'][2]))
	key = ""
	for key,value in p.city.iteritems():
		if value == city_page:
			break

	acc_link = "http://twitter.com/" + key
	max_type = result['post_type_count'][1]['text_only']
	if max_type[0] < result['post_type_count'][2]['images_and_text'][0]:
		max_type = result['post_type_count'][2]['images_and_text']
	if max_type[0] < result['post_type_count'][0]['image_only'][0]:
		max_type = result['post_type_count'][0]['image_only']

	try:
		return render_template("index.html",city=city_page,result = result,acc_link=acc_link,max_type = max_type, values=values, labels=labels,linechart_x=linechart_x, values1=values1, labels1=labels1)
	except Exception, e:
		return str(e)
	

@app.route('/Delhi')
def delhi():
	city_page = "Delhi"
	result = results[city_page]
	
	labels = [result['popular_hastags'][0][0],result['popular_hastags'][1][0],result['popular_hastags'][2][0],
	result['popular_hastags'][3][0],result['popular_hastags'][4][0],result['popular_hastags'][5][0],
	result['popular_hastags'][6][0],result['popular_hastags'][7][0],result['popular_hastags'][8][0],
	result['popular_hastags'][9][0]]
	values = [result['popular_hastags'][0][1],result['popular_hastags'][1][1],result['popular_hastags'][2][1],
	result['popular_hastags'][3][1],result['popular_hastags'][4][1],result['popular_hastags'][5][1],
	result['popular_hastags'][6][1],result['popular_hastags'][7][1],result['popular_hastags'][8][1],
	result['popular_hastags'][9][1]]
	labels1 = ["Text Likes","Text Retweets","Image and Text likes","Image and Text retweets","Image Likes","Image Retweets"]
	values1 = [result['post_type_count'][1]['text_only'][1],result['post_type_count'][1]['text_only'][2],
	result['post_type_count'][2]['images_and_text'][1],result['post_type_count'][2]['images_and_text'][2],
	result['post_type_count'][0]['image_only'][1],result['post_type_count'][0]['image_only'][2]]
	linechart_x = list(range(result['tweet_frequency'][2]))
	key = ""
	for key,value in p.city.iteritems():
		if value == city_page:
			break

	acc_link = "http://twitter.com/" + key
	max_type = result['post_type_count'][1]['text_only']
	if max_type[0] < result['post_type_count'][2]['images_and_text'][0]:
		max_type = result['post_type_count'][2]['images_and_text']
	if max_type[0] < result['post_type_count'][0]['image_only'][0]:
		max_type = result['post_type_count'][0]['image_only']

	try:
		return render_template("index.html",city=city_page,result = result,acc_link=acc_link,max_type = max_type, values=values, labels=labels,linechart_x=linechart_x, values1=values1, labels1=labels1)
	except Exception, e:
		return str(e)		

@app.route('/Kolkata')
def kol():
	city_page = "Kolkata"
	result = results[city_page]
	
	labels = [result['popular_hastags'][0][0],result['popular_hastags'][1][0],result['popular_hastags'][2][0],
	result['popular_hastags'][3][0],result['popular_hastags'][4][0],result['popular_hastags'][5][0],
	result['popular_hastags'][6][0],result['popular_hastags'][7][0],result['popular_hastags'][8][0],
	result['popular_hastags'][9][0]]
	values = [result['popular_hastags'][0][1],result['popular_hastags'][1][1],result['popular_hastags'][2][1],
	result['popular_hastags'][3][1],result['popular_hastags'][4][1],result['popular_hastags'][5][1],
	result['popular_hastags'][6][1],result['popular_hastags'][7][1],result['popular_hastags'][8][1],
	result['popular_hastags'][9][1]]
	labels1 = ["Text Likes","Text Retweets","Image and Text likes","Image and Text retweets","Image Likes","Image Retweets"]
	values1 = [result['post_type_count'][1]['text_only'][1],result['post_type_count'][1]['text_only'][2],
	result['post_type_count'][2]['images_and_text'][1],result['post_type_count'][2]['images_and_text'][2],
	result['post_type_count'][0]['image_only'][1],result['post_type_count'][0]['image_only'][2]]
	linechart_x = list(range(result['tweet_frequency'][2]))
	key = ""
	for key,value in p.city.iteritems():
		if value == city_page:
			break

	acc_link = "http://twitter.com/" + key
	max_type = result['post_type_count'][1]['text_only']
	if max_type[0] < result['post_type_count'][2]['images_and_text'][0]:
		max_type = result['post_type_count'][2]['images_and_text']
	if max_type[0] < result['post_type_count'][0]['image_only'][0]:
		max_type = result['post_type_count'][0]['image_only']

	try:
		return render_template("index.html",city=city_page,result = result,acc_link=acc_link,max_type = max_type, values=values, labels=labels,linechart_x=linechart_x, values1=values1, labels1=labels1)
	except Exception, e:
		return str(e)		

@app.route('/Hyderabad')
def hyd():
	city_page = "Hyderabad"
	result = results[city_page]
	
	labels = [result['popular_hastags'][0][0],result['popular_hastags'][1][0],result['popular_hastags'][2][0],
	result['popular_hastags'][3][0],result['popular_hastags'][4][0],result['popular_hastags'][5][0],
	result['popular_hastags'][6][0],result['popular_hastags'][7][0],result['popular_hastags'][8][0],
	result['popular_hastags'][9][0]]
	values = [result['popular_hastags'][0][1],result['popular_hastags'][1][1],result['popular_hastags'][2][1],
	result['popular_hastags'][3][1],result['popular_hastags'][4][1],result['popular_hastags'][5][1],
	result['popular_hastags'][6][1],result['popular_hastags'][7][1],result['popular_hastags'][8][1],
	result['popular_hastags'][9][1]]
	labels1 = ["Text Likes","Text Retweets","Image and Text likes","Image and Text retweets","Image Likes","Image Retweets"]
	values1 = [result['post_type_count'][1]['text_only'][1],result['post_type_count'][1]['text_only'][2],
	result['post_type_count'][2]['images_and_text'][1],result['post_type_count'][2]['images_and_text'][2],
	result['post_type_count'][0]['image_only'][1],result['post_type_count'][0]['image_only'][2]]
	linechart_x = list(range(result['tweet_frequency'][2]))
	key = ""
	for key,value in p.city.iteritems():
		if value == city_page:
			break

	acc_link = "http://twitter.com/" + key
	max_type = result['post_type_count'][1]['text_only']
	if max_type[0] < result['post_type_count'][2]['images_and_text'][0]:
		max_type = result['post_type_count'][2]['images_and_text']
	if max_type[0] < result['post_type_count'][0]['image_only'][0]:
		max_type = result['post_type_count'][0]['image_only']

	try:
		return render_template("index.html",city=city_page,result = result,acc_link=acc_link,max_type = max_type, values=values, labels=labels,linechart_x=linechart_x, values1=values1, labels1=labels1)
	except Exception, e:
		return str(e)		


if __name__ == "__main__":
	app.run()
	worker()
