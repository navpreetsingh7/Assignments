import re
#A14_Q1
emails = '''zuck26@facebook.com
page33@google.com
jeff42@amazon.com'''

pattern = '(\w*)@([A-Z0-9]*)\.([A-Z]{2,4})'
pat=re.findall(pattern, emails, flags=re.IGNORECASE)

print(pat)

#A14_Q2
text='''
Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter 
better.'''
main= re.findall('[B,b]\w*', text)
print(main)

#A14_Q3
sentence = "A, very very; irregular_sentence"
a=re.compile("[,;_]")
b=a.sub(" ",sentence)
print(b)

#A14_Q4
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
def clean_tweet(tweet):
    tweet = re.sub('http\S*\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

print(clean_tweet(tweet))