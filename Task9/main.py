
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("Sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("Sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("Sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] <= -0.05 :
        print("Negative")
    else :
        print("Neutral")

if __name__ == "__main__" :

    print("\n1st Statement:")
    sentence = input("Enter sentence:")
    sentiment_scores(sentence)

    print("\n2nd Statement:")
    sentence = input("Enter sentence:")
    sentiment_scores(sentence)

    print("\n3rd Statement:")
    sentence = input("Enter sentence:")
    sentiment_scores(sentence)
