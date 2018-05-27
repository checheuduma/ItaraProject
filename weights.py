
def get_weights(retweets,sentiment):
    weight = 10

    if sentiment == 'negative':
        weight *= -1

    if retweets >= 1:
        if retweets <= 10:
            weight *= 0.8
    elif retweets > 10:
        weight *= 0.9
    elif retweets > 100:
        weight *= 0.95
    elif retweets == 0:
        weight *= 0.5

    return weight
