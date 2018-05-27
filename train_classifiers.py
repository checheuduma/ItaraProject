import csv
import nltk
import stopwords
nltk.download('stopwords')
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import string
from nltk.corpus import stopwords
from sklearn.externals import joblib
from classify import processTweet


def create_tfidf(f):
    sentiment = []
    tweet = []

    # Getting original training set
    with open(f, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            # skip missing data
            if row[0] and row[5]:
                if row[0] == '0':
                    sentiment.append('negative')
                elif row[0] == '2':
                    sentiment.append('neutral')
                elif row[0] == '4':
                    sentiment.append('positive')
                tweet.append(processTweet(row[5]))  # .decode('latin-1').encode('utf-8'))
    return tweet,sentiment
    # End


def getStopWordList():
    # read the stopwords file and build a list
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['AT_USER', 'URL', 'url', 'retweet', 'rt']
    return stop


def trainNB(tweets__, sentiments__):
    print ('Vectorizing in process NB...')
    tf = HashingVectorizer(analyzer='word', binary='true', stop_words=getStopWordList(), decode_error='replace',ngram_range=(3, 10))
    clf = BernoulliNB()

    print ('pipelining NB...')
    vec_clf = Pipeline([('tfvec', tf), ('NB', clf)])

    print ('fitting NB...')
    vec_clf.fit(tweets__, sentiments__)

    print ('Dumping to file NB...')
    _ = joblib.dump(vec_clf, 'pickle/Naive Bayes.pkl', compress=9)


def trainSVM(tweets__, sentiments__):
    print ('Vectorizing in process - SVM...')
    tf = HashingVectorizer(analyzer='word', binary='true', stop_words=getStopWordList(), decode_error='replace',
                           ngram_range=(1, 2))

    clf = LinearSVC()

    print ('pipelining - SVM...')
    vec_clf = Pipeline([('tfvec', tf), ('SVM', clf)])

    print ('fitting - SVM...')
    vec_clf.fit(tweets__, sentiments__)

    print ('Dumping to file - SVM...')
    _ = joblib.dump(vec_clf, 'pickle/Support Vector Machine.pkl', compress=9)


def trainMaxEnt(tweets__, sentiments__):
    print ('Vectorizing in process - MaxEnt...')
    tf = HashingVectorizer(analyzer='word', binary='true', stop_words=getStopWordList(), decode_error='replace',
                           ngram_range=(1, 2))

    clf = LogisticRegression()

    print ('pipelining - MaxEnt...')
    vec_clf = Pipeline([('tfvec', tf), ('MaxEnt', clf)])

    print ('fitting - MaxEnt...')
    vec_clf.fit(tweets__, sentiments__)

    print ('Dumping to file - MaxEnt...')
    _ = joblib.dump(vec_clf, 'pickle/Maximum Enthropy.pkl', compress=9)


def load_clf(clf_name):
    print ('Loading ' + clf_name + ' Classifier...')
    classifier = joblib.load('pickle/' + clf_name + '.pkl')
    return classifier


def load_test_data():
    test_sentiment = []
    test_tweet = []

    # Getting test data set
    with open('data/sampleTweets.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        # reader.next()

        for row in reader:
            # skip missing data
            if row[0] and row[1]:
                if row[0] == '|negative|':
                    test_sentiment.append('negative')
                elif row[0] == '|positive|':
                    test_sentiment.append('positive')
                elif row[0] == '|neutral|':
                    test_sentiment.append('neutral')
            test_tweet.append(processTweet(row[1]))  # .decode('latin-1').encode('utf-8'))
    # End
    return test_tweet, test_sentiment


def get_sentiment(tweets, classifier):
    sentiment = []
    for tweet in tweets:
        tweet = processTweet(tweet)
        tweet = [tweet]
        sentiment.append(str(classifier.predict(tweet)[0]))
    return sentiment

def test_accuracy(classifier):
    # Loading the test data
    tweet_test, sentiment_test = load_test_data()

    # Testing the Classifier
    clf = load_clf(classifier)

    # Predict
    sentiment_predicted = get_sentiment(tweet_test, clf)

    # Get Accuracy
    clf_accuracy = "{:.2%}".format(accuracy_score(sentiment_test, sentiment_predicted))
    print ('The accuracy is ' + clf_accuracy)

print ('Reading and pre processing data...')
tweets, sentiments = create_tfidf('data/training.1600000.processed.noemoticon.csv')

trainMaxEnt(tweets, sentiments)

trainNB(tweets, sentiments)

trainSVM(tweets, sentiments)

print ('\nNAIVE BAYES ACCURACY')
test_accuracy('Naive Bayes')

print ('\nMAXIMUM ENTHROPY')
test_accuracy('Maximum Enthropy')

print ('\nSUPPORT VECTOR MACHINE')
test_accuracy('Support Vector Machine')
