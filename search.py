# import csv
# import classify as act
#
# def locdCategories(cTeg='Service'):
#
#     checkCatg = []
#     MainCateg = []
#
#     with open('uploads/TWEETS.csv', 'r', encoding="utf8") as csh:
#         tReader = csv.reader(csh, delimiter=',', quotechar='|')
#         csv.field_size_limit(20000000)
#         for i in tReader:
#             checkCatg.append(i)
#
#     for g in checkCatg:
#         if len(g) > 5 and common_words in g[5]:
#             text = act.processTweet2(g[5])
#             final = act.postprocess(text)
#             sentTweets = act.get_sentiment(final)
#             MainCateg.append([g[1], final, sentTweets])
#         if (len(MainCateg) == 50):
#             break
#
#     return MainCateg