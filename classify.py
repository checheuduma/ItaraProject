import re
from weights import get_weights
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import string

def getStopWordList():
    # read the stopwords file and build a list
    stop = []
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['AT_USER', 'URL', 'url', 'retweet', 'rt']
    return stop

def processTweet(tweet):
    #convert to lower case
    tweet = tweet.lower()
    #convert links to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', tweet)
    #convert @username to AT_user
    tweet = re.sub('@[^\s]+','AT_USER', tweet)
    #remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')
    tweet = re.sub('![^\s]+',' ', tweet)

    return tweet

def processTweet2(tweet):
    #convert to lower case
    tweet = tweet.lower()
    #convert links to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', tweet)
    #convert @username to AT_user
    #tweet = re.sub('@[^\s]+','AT_USER', tweet)
    #remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')
    tweet = re.sub('![^\s]+',' ', tweet)

    return tweet

# Post process tweet to print
def postprocess(tweet):
    # Remove URLS
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)
    # Remove blank lines
    tweet = tweet.replace('\n', ' ')
    # trim
    tweet = tweet.strip('\'"')
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)

    return tweet

def get_sentiment(tweet, classifier):
    tweet = [tweet]
    sentiment = classifier.predict(tweet)[0]
    return sentiment

def evaluate_model(target_true, target_predicted):
    print (classification_report(target_true, target_predicted))
    print ("The accuracy score is {:.2%}".format(accuracy_score(target_true, target_predicted)))

def removeTweetsWithUrl(results):
    # REMOVE TWEETS THAT CONTAINS URL:
    regexp_url = re.compile('((www\.[^\s]+)|(https?://[^\s]+))')

    for result in results:
        if regexp_url.search(result.text) is not None:
            results.remove(result)
    # END OF REMOVAL
    return results

def load_classifier( classifier = 'Support Vector Machine'):
    print ('Loading ' + classifier + ' Classifier...')
    clf = joblib.load('pickle/' + classifier + '.pkl')
    return clf

