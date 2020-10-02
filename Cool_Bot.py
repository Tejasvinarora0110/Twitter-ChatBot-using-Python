import tweepy
print("This is my Twitter bot")


api_key=''#Write your developer api/consumer key
api_secret=''#Write your developer api/consumer secret key
access_key=''#Write your developer access key
access_secret=''#Write your developer access secret key


auth=tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)

file='last_seen id.txt'#this file stores the last seen id


def get_last_id(file):
    fr=open(file,'r')
    last_id=int(fr.read().strip())
    fr.close()
    return last_id

def store_last_id(last_id,file):
    fw=open(file,'w')
    fw.write(str(last_id))
    fw.close()
    return

last_id=get_last_id(file)
mentions=api.mentions_timeline(last_id)

for mention in reversed(mentions):
    print(str(mention.id)+'-'+mention.text)
    last_id=mention.id
    store_last_id(last_id,file)
    if 'Hii' or 'hi' or 'hello' or 'hey' in mention.text.lower():
        print('responding back')
        api.update_status(status='Hey! How are you doing?',in_reply_to_status_id = mention.id,auto_populate_reply_metadata=True)
    
