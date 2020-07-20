from django.shortcuts import render
from django.http import HttpResponse

from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt




# Index view________________________________
def index(request):
    return render(request,'sentiment/index.html')

def result(request):
    if request.method == 'POST':

        # def percentage(part, whole):
        #     return 100 * float(part)/float(whole)

        ConsumerKey = "khpw1yAorQvLakZNBDXdaaI7X"
        ConsumerSecret = "7Gr5fnrAEZ75dLQz8S47bKFAMG1NjxmcKxl9dlup5tDoC5ae6F"
        AccessToken = "2891449368-xZApT2vpyDJVvRSQ2WW5yIx6y3brBu8tOMYMZSz"
        AccessTokenSecret = "6Ck3TDgo3ddJ4WObsSa9S3tqFFFasoDYv00lNAZGlP9jk"

        auth =  tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)
        auth.set_access_token(AccessToken,AccessTokenSecret)
        api = tweepy.API(auth)

        SearchTerm = request.POST.get('searchkey')
        NoOfSearchTerms = 20

        Tweets = tweepy.Cursor(api.search, q=SearchTerm).items(NoOfSearchTerms)

        positive = 0
        negative = 0
        neutral = 0
        polarity = 0
        count = 0

        for tweet in Tweets:
            #print(tweet.text)
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity
            count = count+1


            if (analysis.sentiment.polarity > 0):
                positive += 1
            elif (analysis.sentiment.polarity < 0):
                negative += 1
            elif (analysis.sentiment.polarity == 0):
                neutral += 1

        # positive = percentage(positive, NoOfSearchTerms)
        # negative = percentage(negative, NoOfSearchTerms)
        # neutral = percentage(neutral, NoOfSearchTerms)
        # polarity = percentage(polarity, NoOfSearchTerms)

        positive = format(positive, '.2f')
        negative = format(negative, '.2f')
        neutral = format(neutral, '.2f')

        print("How People are Reacting on " + SearchTerm + " by Analyzing " + str(NoOfSearchTerms) + " Tweets.")

        if (polarity == 0):
            print("neutral")
        elif (polarity < 0.00):
            print("negative")
        elif (polarity > 0.00):
            print("positive")

      
        return render(request,'sentiment/result.html',{'p':positive,'n':negative,'nu':neutral,'searchkey':SearchTerm})




