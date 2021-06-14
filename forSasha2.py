import sys
import csv

# http://www.tweepy.org/
import tweepy

# Get your Twitter API credentials and enter them here
consumer_key = "C3MnSxONlCqpj25d4RU44q8TE"
consumer_secret = "sOHymbVSuM8JvAYiA5Uwa2w39x24CgtO1zN3neEfa2OQyyBLLL"
access_key = "51266046-acyY169hQFDnxtwrIU3XnDky0Wi3Vsp9DxAB2bcAW"
access_secret = "9uvvkt6QeIp4z23NvGVS8O6Y7x6ulsgeYJ8VsTAWEuAUK"


# method to get a user's last tweets
def get_tweets(username):

	# http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# set count to however many tweets you want
	number_of_tweets = 100

	# get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name=username).items(number_of_tweets):
		# create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

# write to a new csv file from the array of tweets
	outfile = username + "_tweets.csv"
	print("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


# if we're running this as a script
if __name__ == '__main__':

	# get tweets for username passed at command line
	if len(sys.argv) == 2:
		get_tweets(sys.argv[1])
	else:
		print("Error: enter one username")
