import tweepy
a=0
b=0
for status in tweepy.Cursor(api.user_timeline).items(50):
    process_status(status)
    status=status.read()
    for x in status.split():
        a+=1
for status in tweepy.Cursor(api.user_timeline).items(50):
    process_status(status)
    status=status.read()
    for x in status.split():
        b+=1
if a>b:
    print("o a exei perissoteres lekseis aptton b")
if b>a:
    print("o b exei perissoteres leskeis apton a")
if a=b:
    print("exoyn idies leskeis")
