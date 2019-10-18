import os
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer
import nltk.corpus
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


def stem_words(f):
    sent_token = sent_tokenize(f)
    print(sent_token)
    word_token=[]
    sent_token1 = ""
    for token in sent_tokenize(f):
        for token1 in word_tokenize(token):
            #print(token1)
            token2 = PorterStemmer().stem(token1)
            word_token.append(token2)
    freq_words(word_token)
    for index,t in enumerate(word_token):
        if index < len(word_token) - 2:
            sent_token1 = sent_token1 + t + " "
        else:
            sent_token1 += t
    return sent_token1  ##  return "".join(word_token

def freq_words(word_token):
    sr = stopwords.words("English")
    wk=word_token[:]
    for t in word_token:
        if t in sr:
            wk.remove(t)
    freq = nltk.FreqDist(wk)
    freq.plot(20)
    plt.show()


#print(os.getcwd())
file = open("C:/Users\Win10\Desktop\Resume.txt")
f=file.read()
print(f)
sw = stem_words(f)
print(sw)
freq_words(sw)


