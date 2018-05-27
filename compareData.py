import csv
import classify as fact

def compA():
    comapareD = []
    with open('uploads/dataA.csv', 'r', encoding="utf8") as dataA:
        tReading = csv.reader(dataA, delimiter = ' ', quotechar = '|')
        csv.field_size_limit(20000000)
        for dRw in tReading:
            text = dRw
            for row in tReading:
                bData = ' '.join(row)
                comapareD.append(bData)
    return comapareD

def compB():
    comapares = []
    with open('uploads/dataB.csv', 'r', encoding="utf8") as dataB:
        tRead = csv.reader(dataB, delimiter = ' ', quotechar = '|')
        csv.field_size_limit(20000000)
        for dRow in tRead:
            text = dRow
            for row in tRead:
                vData = ' '.join(row)
                comapares.append(vData)
    return comapares

def graph():
    new = compA()
    for date in new:
        for i in range(len(new)):
            print(date)


def class_dataA(clf="Support Vector Machine"):
    ts = compA()
    classifier = fact.load_classifier(clf)
    sen = []

    gPlot={'jan':[0,0,0],'feb':[0,0,0],'mar':[0,0,0],'april':[0,0,0],'oct':[0,0,0],'jun':[0,0,0],'jul':[0,0,0],'may':[0,0,0],'aug':[0,0,0],'sep':[0,0,0],'nov':[0,0,0],'dec':[0,0,0]}
    monthtocheck=['jan','feb','mar','april','oct','jun','jul','may','aug','sep','nov','dec']
    postweets = 0
    negtweets = 0

    for t in ts:
        text = fact.processTweet(t)
        try:
            month = text.split(',')[1].split(' ')[1]
            month = month.lower()
            sentiment = fact.get_sentiment(text, classifier)
            if(sentiment == "positive"):
                if month in monthtocheck:
                    gPlot[month][0] += 1
                postweets+=1
            elif(sentiment == "negative"):
                if month in monthtocheck:
                    gPlot[month][1] += 1
                negtweets+=1
        except IndexError:
            continue

    posData = []
    negData = []
    months = ['jan', 'feb', 'mar', 'april', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for month in months:
        posData.append(gPlot[month][0])
        negData.append(gPlot[month][1])
    print(posData, negData)

    pe = (100 * postweets / len(ts))
    ne = (100 * negtweets / len(ts))

    p = format(pe, '.2f')
    n = format(ne, '.2f')


    return posData, negData, p, n

def class_dataB(clf="Support Vector Machine"):
    ts = compB()
    classifier = fact.load_classifier(clf)
    sen = []

    gPlot={'jan':[0,0,0],'feb':[0,0,0],'mar':[0,0,0],'april':[0,0,0],'oct':[0,0,0],'jun':[0,0,0],'jul':[0,0,0],'may':[0,0,0],'aug':[0,0,0],'sep':[0,0,0],'nov':[0,0,0],'dec':[0,0,0]}
    monthtocheck=['jan','feb','mar','april','oct','jun','jul','may','aug','sep','nov','dec']
    postweets = 0
    negtweets = 0

    for t in ts:
        text = fact.processTweet(t)
        try:
            month = text.split(',')[1].split(' ')[1]
            month = month.lower()
            sentiment = fact.get_sentiment(text, classifier)
            if(sentiment == "positive"):
                if month in monthtocheck:
                    gPlot[month][0] += 1
                postweets+=1
            elif(sentiment == "negative"):
                if month in monthtocheck:
                    gPlot[month][1] += 1
                negtweets+=1
        except IndexError:
            continue

    posData = []
    negData = []
    months = ['jan', 'feb', 'mar', 'april', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for month in months:
        posData.append(gPlot[month][0])
        negData.append(gPlot[month][1])
    print(posData, negData)


    pe = (100 * postweets / len(ts))
    ne = (100 * negtweets / len(ts))

    p = format(pe, '.2f')
    n = format(ne, '.2f')

    return posData, negData, p, n


def class_dataB_test(clf="Support Vector Machine"):
    ts = []
    classifier = fact.load_classifier(clf)

    with open('uploads/dataB.csv', 'r', encoding="utf8") as wash:
        tReader = csv.reader(wash, delimiter=',', quotechar='|')
        csv.field_size_limit(20000000)
        for i in tReader:
            ts.append(i)

    gPlot={'jan':[0,0,0],'feb':[0,0,0],'mar':[0,0,0],'april':[0,0,0],'oct':[0,0,0],'jun':[0,0,0],'jul':[0,0,0],'may':[0,0,0],'aug':[0,0,0],'sep':[0,0,0],'nov':[0,0,0],'dec':[0,0,0]}
    monthtocheck=['jan','feb','mar','april','oct','jun','jul','may','aug','sep','nov','dec']
    postweets = 0
    negtweets = 0

    for t in ts:
        # text = fact.processTweet(t)
        if len(t) > 5:
            text = t[5]
            try:
                #month = text.split(',')[1].split(' ')[1]
                month = t[1]
                month = month.lower()
                print(month)

                sentiment = fact.get_sentiment(text, classifier)
                if(sentiment == "positive"):
                    if month in monthtocheck:
                        gPlot[month][0] += 1
                    postweets+=1
                elif(sentiment == "negative"):
                    if month in monthtocheck:
                        gPlot[month][1] += 1
                    negtweets+=1
            except IndexError:
                continue

    positives = []
    negatives = []
    months = ['jan', 'feb', 'mar', 'april', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for month in months:
        positives.append(gPlot[month][0])
        negatives.append(gPlot[month][1])
    #print(positives, negatives)

    return positives, negatives

# print('\n')
# class_dataB()