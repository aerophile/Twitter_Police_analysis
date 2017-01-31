import extract_tweets
import parameters
from process_tweets import process_tweets_function


results = {'Mumbai': {'popular_hastags': [(u'TrafficAlert', 4), (u'WeThePolice', 4), (u'traffic', 4), (u'TrafficUpdateMumbai', 3), (u'FactsvsAlternativeFacts', 2), (u'Mumbai', 2), (u'MumbaiTraffic', 2), (u'LalbaugFlyover', 2), (u'Traffic', 2), (u'Umang2017', 2)], 'post_type_count': [{'image_only': [0, 0, 0, ' Image only Posts']}, {'text_only': [22, 3653, 1403, 'Text posts']}, {'images_and_text': [10, 2381, 447, 'Image and Text Posts']}], ' sentiment_result_list': [12, 66, 22], 'tweet_frequency': [2.99, [69.34, 7.98, 8.83, 10.9, 14.77, 51.37, 477.35, 2.15, 4.63, 4.79, 17.28, 25.29, 27.14, 1.4, 5.21, 1.07, 1.2, 3.76, 1.28, 96.54, 1.67, 3.1, 10.43, 12.12, 1.55, 2.85, 1.31, 7.1, 1.09, 0.9, 6.25], 31]},
			'Delhi': {'popular_hastags': [(u'BeRainSafe', 4), (u'RepublicDay', 2), (u'IndependenceDay2016', 1), (u'DontDrinkAndDrive', 1), (u'Don', 1), (u'BeAlertBeSafe', 1), (u'HAPPYNEWYEAR', 1), (u'happynewyear', 1), (u'EyesAndEars', 1),(u'Dial100', 1)], 'post_type_count': [{'image_only': [0, 0, 0, ' Image only Posts']}, {'text_only': [89, 3102, 1352, 'Text posts']}, {'images_and_text': [33, 6601, 6373, 'Image and Text Posts']}], ' sentiment_result_list': [37, 45, 18], 'tweet_frequency': [0.7, [0.26, 1.07, 0.82, 122.73, 0.94, 0.07, 0.36, 0.17, 51.77, 11.02, 206.21, 0.13, 49.4, 3.66, 0.16, 0.17, 0.34, 0.21, 0.32, 0.31, 7.34, 67.5, 3200.0, 69.85, 0.13, 0.45, 1.28, 23.26, 0.78, 32.7, 0.53, 1.84, 11.36, 6.77, 2.41, 2.1, 0.5, 5.36, 0.43, 2.25, 6.1, 640.0, 1728.0, 8.09, 654.55, 81.66, 1.45, 2.3, 9.35, 1.01, 1.92, 1489.66, 1.1, 3.85, 1489.66, 3600.0, 1515.79, 2700.0, 138.68, 0.54, 3.09, 0.1, 29.22, 0.32, 0.78, 0.5, 289.93, 2.02, 114.74, 3.34, 0.31, 0.39, 48.62, 1.1, 0.25, 14.64, 1.3, 5.78, 1.98, 1.62, 48.62, 438.58, 7.16, 105.11, 0.54, 0.99, 84.79, 0.26, 0.79, 1.1, 1.05, 1.16, 72.42, 121.18, 0.2, 0.16, 0.79, 46.25, 140.49, 154.56, 0.37, 0.35, 1.96, 0.54, 9.66, 467.03, 204.74, 68.14, 0.27, 1080.0, 0.19, 0.66, 0.22, 0.28, 24.48, 1.1, 4.16, 5.16, 60.67, 348.39, 1.58], 121]},
			'Kolkatta': {'popular_hastags': [(u'KPTrafficUpdate', 113), (u'KPTrafficRegulations', 28), (u'PROBAHO', 27), (u'RoadSafetyWeek', 17), (u'CrimeDetection', 13), (u'TrafficAwareness', 11), (u'CyberSafety', 10), (u'KPSecurityAdvisory', 9), (u'SafeDriveSaveLife', 9), (u'SafeDriveSavesLife', 5)], 'post_type_count': [{'image_only': [8, 134, 55, ' Image only Posts']}, {'text_only': [207, 2517, 1434, 'Text posts']}, {'images_and_text': [145, 2450, 908, 'Image and Text Posts']}], ' sentiment_result_list': [26, 38, 36], 'tweet_frequency': [0.98, [0.25, 0.36, 19.99, 15.48, 48.76, 1.03, 0.32, 0.81, 0.15, 1.11, 568.42, 1.0, 1.44, 0.31, 0.35, 0.24, 0.46, 1838.3, 0.37, 3.21, 0.59, 64.48, 0.14, 0.19, 0.53, 0.91, 1.6, 0.3, 0.54, 0.49, 0.2, 0.2, 0.48, 0.25, 2700.0, 0.49, 0.55, 0.91, 0.21, 0.83, 0.26, 31.44, 0.31, 0.17, 378.95, 738.46, 0.82, 0.36, 0.24, 0.98, 21.2, 0.2, 1093.67, 1.13, 10.4, 0.17, 0.24, 0.36, 0.9, 0.34, 0.32, 0.99, 1.05, 4.32, 0.33, 0.57, 19.37, 14.91, 28.95, 6171.43, 0.48, 0.21, 0.14, 1.06, 10.39, 1.27, 7.09, 1.17, 4547.37, 3.9, 0.91, 1.12, 0.52, 9.87, 0.15, 0.14, 9.86, 2541.18, 0.55, 0.46, 0.35, 0.92, 0.52, 0.25, 0.26, 5.7, 32.11, 1.01, 0.51, 0.47, 1.47, 3.13, 0.99, 0.35, 0.47, 0.2, 1.13, 21.76, 0.24, 41.4, 0.53, 0.31, 0.26, 7.83, 1.3, 12.62, 0.17, 0.49, 374.03, 1136.84, 0.2, 26.06, 0.24, 9.44, 55.96, 1.7, 0.32, 261.82, 0.51, 80.67, 122.21, 561.04, 0.45, 0.33, 1.0, 1.0, 1.0, 0.05, 195.03, 0.86, 0.52, 0.56, 0.96, 17.59, 1.06, 0.89, 477.35, 0.32, 1.02, 0.55, 0.99, 0.34, 0.83, 1.31, 16.42, 110.2, 981.82, 1.08, 25.94, 423.53, 8.81, 6.76, 1.16, 179.63, 1371.43, 6.59, 0.55, 7.93, 517.37, 0.96, 0.97, 34.64, 1.11, 1.24, 15.28, 5.36, 726.05, 1.01, 211.76, 1080.0, 0.56, 7.06, 62.79, 123.43, 1183.56, 1.24, 4.62, 345.6, 1.45, 11.23, 18.41, 125.22, 7.99, 28.12, 1.34, 205.23, 467.03, 5.3, 1.3, 394.52, 292.88, 474.73, 3.54, 1.0, 0.55, 318.82, 8.04, 154.56, 1080.0, 1309.09, 316.48, 0.96, 564.71, 1.38, 276.92, 226.18, 83.56, 2400.0, 3.91, 1.48, 42.79, 4.04, 17.85, 1.57, 23.54, 3.27, 272.56, 169.41, 0.34, 0.97, 423.53, 1838.3, 1.3, 4.61, 0.98, 1.01, 1066.67, 1.0, 0.54, 9.88, 0.97, 0.99, 401.86, 530.06, 1.02, 281.43, 0.99, 1.0, 0.55, 7.16, 0.99, 76.73, 0.99, 1838.3, 1.0, 276.92, 960.0, 1.12, 141.41, 9.46, 1.0, 0.54, 9.61, 1.32, 11.35, 5.16, 257.91, 1.31, 550.32, 25.59, 5.1, 2700.0, 523.64, 557.42, 1.52, 13.58, 12.5, 5.49, 1.39, 165.2, 5.01, 282.35, 1.19, 152.92, 106.01, 4.73, 2.08, 11.14, 1728.0, 778.38, 0.78, 8.58, 1.7, 0.8, 1.03, 5.86, 115.2, 23.28, 1.34, 22.45, 151.85, 1004.65, 0.97, 6.48, 1.31, 0.93, 8.01, 6.16, 1515.79, 65.31, 1.41, 7.57, 890.72, 7.06, 214.39, 1.87, 10.92, 764.6, 900.0, 16.82, 36.55, 17.82, 1800.0, 12.85, 3323.08, 1542.86, 54.2, 176.33, 1489.66, 1234.29, 708.2, 1.99, 5.02, 13.63, 301.05, 24.17, 855.45, 9.23, 11.77, 685.71, 1.26, 2.46, 2.22, 11.56, 116.91, 352.65, 9.11, 6.93, 71.76, 630.66, 398.16, 0.96, 1.34, 4320.0, 5082.35, 4800.0, 1200.0], 357]},
			'Hyderabad': {'popular_hastags': [(u'Hyderabadcitypolice', 13), (u'RepublicDay', 6), (u'Hyderabad', 5), (u'HawkEye', 5), (u'ReportUs', 4), (u'StopViolenceAgainstWomen', 3), (u'Republicday', 3), (u'Dial100', 3), (u'BeSafe', 3), (u'MobileApp', 3)], 'post_type_count': [{'image_only': [138, 1436, 489, ' Image only Posts']}, {'text_only': [107, 1093, 331, 'Text posts']}, {'images_and_text': [92, 1340, 418, 'Image and Text Posts']}], ' sentiment_result_list': [33, 20, 46], 'tweet_frequency': [7.52, [3.57, 2.21, 680.31, 218.18, 405.63, 664.62, 1489.66, 2.33, 4.9, 12.97, 14.0, 13.44, 8.6, 2618.18, 7200.0, 5760.0, 3200.0, 4547.37, 2.86, 18.41, 3.46, 10.24, 12.19, 15.34, 2273.68, 4114.29, 1.05, 7.99, 5400.0, 2.82, 5.66, 35.9, 12.12, 7.98, 4.15, 7200.0, 4320.0, 4547.37, 1.38, 20.64, 1289.55, 6171.43, 2700.0, 120.84, 1878.26, 8.86, 165.52, 65.31, 3200.0, 8640.0, 2.89, 4.23, 1.86, 1107.69, 5082.35, 1800.0, 6171.43, 1838.3, 3.02, 18.48, 91.04, 7.36, 7.08, 3.99, 10800.0, 3200.0, 8640.0, 1.45, 7.32, 44.35, 15.27, 22.44, 1.58, 17.11, 18.77, 11.03, 5.19, 10800.0, 7854.55, 1.53, 7.89, 9.01, 15.64, 12.91, 12342.86, 2.0, 10.8, 6.92, 23.66, 20.6, 9.88, 659.54, 257.91, 2.42, 84.13, 3.89, 20.25, 105.49, 28.82, 7.97, 5.56, 3085.71, 2979.31, 190.73, 3456.0, 2.41, 7.99, 5.25, 10.83, 34.87, 7.88, 1028.57, 4800.0, 14400.0, 12342.86, 2.27, 14400.0, 1152.0, 6.42, 12.65, 6.56, 20.67, 49.23, 110.34, 8.43, 2.07, 14.94, 4.62, 15.05, 7.59, 7854.55, 2.13, 2.98, 5.71, 1.39, 4.73, 51.12, 61.71, 159.41, 222.11, 2.33, 2.3, 6.1, 1489.66, 557.42, 327.27, 2.74, 720.0, 696.77, 4.55, 8.85, 3.19, 98.52, 1542.86, 2.45, 2.51, 8.2, 283.28, 1.68, 22.72, 12.31, 31.24, 73.78, 8.79, 19.88, 6.95, 2.01, 7.91, 3.04, 97.3, 170.75, 1.59, 8.39, 4.96, 1.54, 54.03, 15.88, 8.36, 7.7, 95.26, 107.87, 102.61, 981.82, 561.04, 1.74, 19.22, 12.62, 12.81, 16.32, 4.44, 380.62, 8640.0, 2335.14, 47.11, 2.42, 21.35, 15.32, 2.69, 120.84, 691.2, 3.39, 3.85, 11.16, 8.25, 3.49, 2700.0, 372.41, 2.31, 13.54, 11.68, 37.84, 18.82, 7.58, 19.69, 5.4, 1.69, 6.66, 26.97, 12.65, 10.35, 2700.0, 2057.14, 1040.96, 1.91, 1028.57, 2.23, 8640.0, 3.79, 69.62, 23.7, 8.03, 77.98, 9.24, 13.18, 6.67, 4.95, 3323.08, 496.55, 1080.0, 1200.0, 2.1, 25.06, 53.83, 73.85, 372.41, 109.23, 151.58, 309.68, 49.2, 8.35, 60.59, 38.08, 32.19, 31.18, 6.96, 960.0, 392.73, 474.73, 2.75, 472.13, 4.78, 8.36, 61.54, 9.77, 10.9, 5.08, 3085.71, 176.69, 2.96, 20.01, 10.81, 17.72, 4.77, 4320.0, 11.0, 9.67, 380.62, 2700.0, 1.97, 369.23, 7.64, 30.85, 5.33, 11.34, 99.31, 1.94, 99.08, 5.92, 5.77, 29.57, 3.62, 10800.0, 3.55, 4.16, 2.83, 114.59, 324.81, 3085.71, 1152.0, 3756.52, 1.07, 1.58, 82.29, 27.07, 4.36, 12.24, 131.31, 2.01, 5.59, 7.61, 4.15, 8640.0, 210.73, 2979.31, 3927.27, 2057.14, 2.89, 6.92, 3.97, 5.2, 490.91, 1.31, 10.36, 21.85, 10.4, 5760.0, 1.92, 5.32, 8.1, 9.79, 8.47, 95.68, 2.34, 2.11, 25.62], 335]},
			'Bangalore': {'popular_hastags': [(u'NYE2017', 33), (u'eLostReport', 10), (u'BewareFraud', 10), (u'RepublicDay', 8), (u'Dial100', 8), (u'CyberAware', 7), (u'BCP', 7), (u'DIAL100', 7), (u'Begging', 6), (u'FollowTrafficRules', 6)], 'post_type_count': [{'image_only': [2, 106, 40, ' Image only Posts']}, {'text_only': [162, 6083, 2709, 'Text posts']}, {'images_and_text': [155, 6228, 2103, 'Image and Text Posts']}], ' sentiment_result_list': [28, 44, 28], 'tweet_frequency': [6.32, [4547.37, 41.96, 160.89, 8.91, 1878.26, 4.5, 1.44, 21.29, 226.18, 3.83, 1.21, 39.8, 1.15, 38.16, 13.88, 259.46, 0.9, 220.97, 226.18, 0.84, 25.43, 751.3, 1252.17, 46.68, 1.71, 115.97, 4320.0, 185.01, 1167.57, 1440.0, 5082.35, 13.22, 104.73, 168.42, 43.75, 0.91, 40.53, 1.34, 6.44, 51.34, 1.26, 0.83, 1.11, 3456.0, 24.06, 33.64, 11.49, 21.67, 34.42, 1107.69, 778.38, 621.58, 785.45, 1.43, 6.25, 363.03, 12.25, 1.29, 3.55, 429.85, 2.01, 2.34, 157.66, 12.37, 361.51, 183.44, 1694.12, 290.91, 1.7, 3.29, 691.2, 1.13, 1.12, 2.51, 2.0, 254.12, 2618.18, 1093.67, 5.74, 11.69, 691.2, 2468.57, 321.19, 233.51, 16.05, 69.68, 6646.15, 3600.0, 3085.71, 1.63, 2.86, 1.56, 8.5, 19.09, 251.9, 2541.18, 80.07, 27.61, 11.12, 48.08, 771.43, 61.49, 81.59, 217.09, 1694.12, 385.71, 1.22, 872.73, 1270.59, 4.41, 738.46, 583.78, 348.39, 664.62, 9.55, 1.56, 8.46, 93.0, 89.91, 526.83, 58.98, 1.11, 550.32, 0.92, 17.43, 3200.0, 3927.27, 3456.0, 19.07, 1.27, 1.41, 7.8, 2618.18, 46.06, 107.73, 649.62, 241.34, 0.73, 1.33, 0.94, 33.26, 42.9, 1.36, 17.38, 262.61, 1.47, 328.52, 407.55, 502.33, 71.29, 469.57, 450.0, 617.14, 4.04, 41.54, 526.83, 425.62, 103.72, 112.35, 212.81, 313.04, 111.92, 1200.0, 480.0, 390.95, 204.74, 1004.65, 164.26, 34.07, 24.68, 129.92, 238.02, 219.85, 508.24, 132.52, 1440.0, 680.31, 37.03, 226.18, 44.72, 1.47, 14.36, 27.72, 67.98, 1093.67, 151.31, 86.4, 267.49, 564.71, 57.41, 216.54, 815.09, 143.76, 18.01, 14.78, 1.39, 6.13, 171.09, 56.03, 37.03, 27.62, 14.44, 2160.0, 92.21, 157.38, 182.66, 34.11, 78.19, 2.4, 3.05, 1.05, 4.45, 95.26, 407.55, 219.85, 6.24, 1.72, 10.9, 3.82, 792.66, 3085.71, 1200.0, 3323.08, 3600.0, 1.25, 0.52, 23.85, 244.07, 286.09, 26.98, 1289.55, 38.37, 12.67, 568.42, 960.0, 1107.69, 327.27, 778.38, 57.72, 1.52, 5.16, 17.9, 1.13, 20.23, 179.25, 176.33, 6.02, 46.63, 1.66, 14.12, 18.32, 3756.52, 3200.0, 7200.0, 8.25, 847.06, 91.04, 1252.17, 2273.68, 1.49, 13.83, 6.91, 159.12, 523.64, 14.63, 28.86, 71.4, 72.06, 26.44, 738.46, 26.34, 1.7, 119.83, 8.81, 0.53, 425.62, 6.73, 520.48, 1.1, 7.44, 283.28, 11.61, 55.03, 34.94, 49.8, 244.07, 294.88, 78.76, 502.33, 7200.0, 5760.0, 2160.0, 7.17, 1.63, 14.28, 83.56, 6.77, 264.22, 186.21, 1.05, 19.55, 8.62, 86.66, 235.42, 830.77, 1.77, 109.78, 10.95, 19.4, 564.71, 20.22, 27.7, 168.09, 53.93, 342.86, 263.41], 316]}
			}



def produce_result():
	for handle in parameters.handles:
		
		tweet_list = extract_tweets.obtain_tweets(handle)
		#extract_tweets.print_tweet_text(tweet_list)
		result = process_tweets_function(tweet_list,handle)
		#print result
		results[parameters.city[handle]] = result
	return results


