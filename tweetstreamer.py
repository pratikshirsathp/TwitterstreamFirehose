import tweepy
from tweepy import streaming
import twitter_credentials
import boto3
import json

"""create a boto3 session if cli is already configured no need to
    put parameters
""" 
session = boto3.Session(aws_access_key_id="your aws access key id", 
aws_secret_access_key="your aws secret access key ", aws_session_token="",
region_name="", botocore_session="", profile_name="")

#firehose client
clientfirehose =session.client('firehose')

#function to send data to firehose
def send_to_stream(data):

    response = clientfirehose.put_record(
        DeliveryStreamName = "twitterstream",
        Record = {
            'Data' : data
        }
    )
    return response

#class that uses twitter api and gets real time tweets
class tweetstreamer(streaming.Stream):

    def on_data(self, data):
        print(data)
        response = send_to_stream(data)
        return True

    def on_status(self, status):
        return (status)

#stream instance of tweetstreamer class

stream = tweetstreamer(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET,
    twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET
    )
#filtering tweets
stream.filter(track=["aws","bigdata","python"])

#awssender = awsSender()
#awssender.send_to_stream()
