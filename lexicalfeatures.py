from nltk.tokenize import word_tokenize
from collections import defaultdict
from readFiles import*
import operator
import re

def extractBagOfWords(document, dictionary, train):
        counts=defaultdict(int)
        lines=document.split("\n")
        for line in lines:
            words=word_tokenize(line)
            for word in words:
                word=word.lower().strip(".")
                if train:
                    if word not in dictionary:
                        dictionary.append(word)
                    counts[word]+=1
                elif word in dictionary:
                    counts[word]+=1
        return counts, dictionary

def organizeBOW(counts, dictionary):
    resp=[]
    for word in dictionary:
        resp.append(counts[word])
    return resp

def bulkBagOfWords(trainitems, testitems):
    dictionary=[]
    traincounts=[]
    for item in trainitems:
        features, dictionary= extractBagOfWords(item, dictionary,True)
        traincounts.append(features)
    trainfeatures=[]
    for counts in traincounts:
        trainfeatures.append(organizeBOW(counts, dictionary))
    testcounts=[]
    for item in testitems:
        counts, dictionary= extractBagOfWords(item, dictionary,False)
        testcounts.append(counts)
    testfeatures=[]
    for counts in testcounts:
        testfeatures.append(organizeBOW(counts, dictionary))
    return trainfeatures, testfeatures, dictionary

#modify if we're gonna use
def arangeLexicon(lexicon,countdicts,num=None):
    sorted_pairs = sorted(lexicon.items(), key=operator.itemgetter(1))
    sorted_pairs.reverse()
    org_lexicon=[elem[0] for elem in sorted_pairs ]
    if num:
        org_lexicon=org_lexicon[:num]
    features=[]
    for counts in countdicts:
        features.append(organizeBOW(counts,org_lexicon))
    return features,org_lexicon


def extractNgrams(document, lexicon, train, n):
    counts=defaultdict(int)
    lines=document.split("\n")
    for line in lines:
        words=["#"]*(n-1)
        words+=word_tokenize(line)
        words+=["#"]*(n-1)
        for ind in range(len(words)-(n-1)):
            ngram=" ".join(words[ind:ind+n])
            if train:
                counts[ngram]+=1
                lexicon[ngram]+=1
            elif ngram in lexicon:
                counts[ngram]+=1
    return counts, lexicon

def bulkNgrams(trainitems, testitems, n):
    dictionary=defaultdict(int)
    traincounts=[]
    #train items
    for item in trainitems:
        features, dictionary= extractNgrams(item, dictionary,True,n)
        traincounts.append(features)
    trainfeatures,lexicon=arangeLexicon(dictionary,traincounts)
    testcounts=[]
    #test items
    for item in testitems:
        counts, dictionary= extractNgrams(item, dictionary,False,n)
        testcounts.append(counts)
    testfeatures=[]
    for count in testcounts:
        testfeatures.append(organizeBOW(count,lexicon))
    return trainfeatures, testfeatures, dictionary