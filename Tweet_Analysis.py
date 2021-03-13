from textblob import TextBlob
import csv
import tweepy
import unidecode
import argparse



# AUTHENTICATION (OAuth)
f = open('auth.k','r')
ak = f.readlines()
f.close()
auth1 = tweepy.auth.OAuthHandler(ak[0].replace("\n",""), ak[1].replace("\n",""))
auth1.set_access_token(ak[2].replace("\n",""), ak[3].replace("\n",""))
api = tweepy.API(auth1)

# Tweeter search with keyword
def tw_parser():
    global qw, ge, l, t, c, d

# USE EXAMPLES:
# =-=-=-=-=-=-=
# % twsearch <search term>            --- searches term
# % twsearch <search term> -c 12      --- searches term and returns 12 tweets (count=12) <DEFAULT = 1>
# % twsearch <search term> -o {ca, tx, id, co, rtc)   --- searches term and sets output options <DEFAULT = ca, tx>

# Parse the command
    parser = argparse.ArgumentParser(description='Twitter Search')
    parser.add_argument(action='store', dest='query', help='Search term string')
    parser.add_argument('-c', action='store', dest='c', help='Tweet count (must be < 100)')
    args = parser.parse_args()

    qw = args.query     # Actual query word(s)
    cmax = 1000
    # Tweet count
    if args.c:
        c = int(args.c)
        if (c > cmax):
            print ("Resetting count to ",cmax," (maximum allowed)")
            c = cmax
        if (not (c) or (c < 1)):
            c = 1
    if not(args.c):
        c = 1
tw_parser()
csvFile = open('Twitter_result.csv','a+',encoding = 'utf-8')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","author id","created", "text", "retwc", "hashtag", "followers", "friends","polarity","subjectivity"])
counter = 0

for tweet in tweepy.Cursor(api.search, q = qw, count = c).items():
    created = tweet.created_at
    text = tweet.text
    text = unidecode.unidecode(text) 
    retwc = tweet.retweet_count
    try:
        hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
    except:
        hashtag = "None"
    username  = tweet.author.name            #author/user name
    authorid  = tweet.author.id              #author/user ID#
    followers = tweet.author.followers_count #number of author/user followers (inlink)
    friends = tweet.author.friends_count     #number of author/user friends (outlink)

    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    csvWriter.writerow([username, authorid, created, text, retwc, hashtag, followers, friends, polarity, subjectivity])

    counter = counter + 1
    if (counter == c):
        break
    
csvFile.close()
