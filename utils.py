import csv
import classify as act
allow = set(['txt', 'csv'])

def getTweetFromFile():
    filetoreturn=[]
    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as csf:
        tReader = csv.reader(csf, delimiter = ' ', quotechar = '|')
        csv.field_size_limit(20000000)
        for row1 in tReader:
            text = row1
            for row in tReader:
                vals = ' '.join(row)
                filetoreturn.append(vals)
    return filetoreturn

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allow

def classify__(clf="Support Vector Machine"):

    ts = getTweetFromFile()
    getIt = len(ts)
    classifier = act.load_classifier(clf)
    avgPos = []
    avgNeg = []

    gPlot={'jan':[0,0,0],'feb':[0,0,0],'mar':[0,0,0],'april':[0,0,0],'oct':[0,0,0],'jun':[0,0,0],'jul':[0,0,0],'may':[0,0,0],'aug':[0,0,0],'sep':[0,0,0],'nov':[0,0,0],'dec':[0,0,0]}
    monthtocheck=['jan','feb','mar','april','oct','jun','jul','may','aug','sep','nov','dec']
    postweets = 0
    negtweets = 0
    neutral = 0

    for t in ts:
        text = act.processTweet(t)
        try:
            month = text.split(',')[1].split(' ')[1]
            month = month.lower()
            sentiment = act.get_sentiment(text, classifier)
            if sentiment == "positive":
                if month in monthtocheck:
                    gPlot[month][0] += 1
                postweets += 1
            elif sentiment == "negative":
                if month in monthtocheck:
                    gPlot[month][1] += 1
                negtweets += 1
            else:
                if month in monthtocheck:
                    gPlot[month][2] += 1
                neutral += 1
        except IndexError:
            continue
    # for sent in sentiment:
    #     if sentiment == "neutral":
    #         sen.append(sent)


    # print(gPlot)
    # print("Positive tweets percentage: {} %".format(100 * postweets / len(ts)))
    # print("Negative tweets percentage: {} %".format(100 * negtweets / len(ts)))
    # print("Neutral tweets percentage: {} %".format(100 * (len(ts) - negtweets - postweets) / len(ts)))

    p = (100 * postweets / len(ts))
    n = (100 * negtweets / len(ts))
    ne = (100 * (len(ts) - negtweets - postweets) / len(ts))

    if(p < n):
        print("Negative")
    elif( p > n):
        print("Positive")
    else:
        print("Neutral")

    pe = format(p, '.2f')
    nee = format(n, '.2f')
    neu = format(ne, '.2f')

    positives = []
    negatives = []
    neutrals = []
    months = ['jan', 'feb', 'mar', 'april', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for month in months:
        positives.append(gPlot[month][0])
        negatives.append(gPlot[month][1])
        neutrals.append(gPlot[month][2])

    for ee, gg in gPlot.items():
        avgPos.append(gg[0])
        avgNeg.append(gg[1])

    aPos = sum(avgPos) / len(ts)
    aNeg = sum(avgNeg) / len(ts)

    avPos = format(aPos, '.4f')
    avNeg = format(aNeg, '.4f')

    return pe , nee, neu, positives, negatives, neutrals, avPos, avNeg, getIt

def common_words():

    s = []
    sa = []

    with open('stopwords.txt', 'r') as lane:
        lan2 = lane.readlines()
        for line in lan2:
            inner = [elt.strip() for elt in line.split(' ')]
            sa.append(inner)

        sa = [j for i in sa for j in i]

    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as csh:
        tReader = csv.reader(csh, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            s.append(i)

    d = {}

    for z in s:
        if len(z) > 5:
            wlow = z[5].lower().split(' ')
            whigh = z[1]
            for w in wlow:
                if w not in sa:
                    if(w in d):
                        d[w] += 1

                    else:
                        d[w] = 1

    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()

    why = []
    why2 = []
    # why3 = []

    for count, word in lst[:5]:
        why.append(count)
        why2.append(word)
        # why3.append(dat)
        print('%4s %s ' % (count, word))


    ''' This for loops below help to individually collect the number of words
    and the words in order to plot them in the pie chart
    '''
    for cut in range(len(why)):
        cut1 = why[0]
        cut2 = why[1]
        cut3 = why[2]
        cut4 = why[3]
        cut5 = why[4]

    for cutt in range(len(why2)):
        cutt1 = why2[0]
        cutt2 = why2[1]
        cutt3 = why2[2]
        cutt4 = why2[3]
        cutt5 = why2[4]

    cal = (cut1 / len(s))
    cal2 = (cut2 / len(s))
    cal3 = (cut3 / len(s))
    cal4 = (cut4 / len(s))
    cal5 = (cut5 / len(s))

    #.......................#

    call = format(cal, '.2f')
    call2 = format(cal2, '.2f')
    call3 = format(cal3, '.2f')
    call4 = format(cal4, '.2f')
    call5 = format(cal5, '.2f')

    Mega = []
    for c in why2:
        Mega = list(Top_tweets(c)) + Mega

    return call, call2, call3, call4, call5, cutt1, cutt2, cutt3, cutt4, cutt5, Mega

def Top_tweets(common_words):

    top_tweets = []
    final_list = []

    getSentiment = act.load_classifier()

    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as wash:
        tReader = csv.reader(wash, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            top_tweets.append(i)

    for g in top_tweets:
        if len(g) > 5 and common_words in g[5]:
            text = act.processTweet2(g[5])
            final = act.postprocess(text)
            sentTweets = act.get_sentiment(final, getSentiment)
            final_list.append([g[1], final,sentTweets])
        if(len(final_list) == 10):
            break

    return final_list

def Track():

    rateTrack = []
    rating = []

    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as csh:
        tReader = csv.reader(csh, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            rateTrack.append(i)

    for g in rateTrack:
        if len(g) > 5:
            rating.append([g[1]])
        if(len(rating) > len(rateTrack)):
            break
        else:
            continue
    rating = [j for i in rating for j in i]
    # got = len(rating)
    front = rating[-1:]
    back = rating[1:2]

    return front, back

def caTe(categories="categories"):

    confirm = []
    classifier = act.load_classifier()
    holdOn = []

    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as wash:
        tReader = csv.reader(wash, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            confirm.append(i)

    for conF in confirm:
        if len(conF) > 5 and categories in conF[5]:
            text = act.processTweet2(conF[5])
            sentiment = act.get_sentiment(text, classifier)
            holdOn.append([text, sentiment])
        if len(holdOn) == 10:
            break
    return holdOn

def viewMore(monthData, sentData):

    more = []
    classifier = act.load_classifier()
    collectData = []

    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as wash:
        tReader = csv.reader(wash, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            more.append(i)

    for vMore in more:
        if len(vMore) > 5 and monthData in vMore[1]:
            text = act.processTweet2(vMore[5])
            sentiment2 = act.get_sentiment(text, classifier)
            if(sentiment2 == sentData):
                collectData.append([vMore[1],text, sentiment2])
        if len(collectData) == 10:
            break
    return collectData

def span( common_words):

    top_tweets = []
    final_list = []

    getSentiment = act.load_classifier()

    with open('uploads/TWEETS.csv', 'r', encoding="utf8") as wash:
        tReader = csv.reader(wash, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            top_tweets.append(i)

    for g in top_tweets:
        if len(g) > 5 and common_words in g[5]:
            text = act.processTweet2(g[5])
            final = act.postprocess(text)
            sentTweets = act.get_sentiment(final, getSentiment)
            final_list.append([g[1], final, sentTweets])
        if (len(final_list) == 10):
            break
    date = []

    for span in top_tweets:
        if len(span) > 5 and common_words in span[5]:
            date.append(span[1])
        if (len(date) == len(top_tweets)):
            break
    Fdate = date[1:2]
    Bdate = date[-1:]
    return [Fdate, Bdate]