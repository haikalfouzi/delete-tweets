import twitter
filename = './bad tweets/tweet_id.json'
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

tweet_id = lines = open(filename).read().splitlines()

if __name__=="__main__":
    for i in tweet_id:
        api.DestroyStatus(int(i))
