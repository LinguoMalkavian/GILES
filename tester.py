from lexicalfeatures import *
from sklearn import svm

masterlist=readFiles()
mainchars=["BUFFY", "WILLOW", "XANDER", "GILES"]
testcounts={"BUFFY":0,"WILLOW":0,"XANDER":0,"GILES":0}
testitems=[]
testlabels=[]
trainitems=[]
trainlabels=[]
for pair in masterlist:
    label=pair[0]
    script=pair[1]
    if testcounts[label]<10:
        testitems.append(script)
        testlabels.append(label)
        testcounts[label]+=1
    else:
        trainitems.append(script)
        trainlabels.append(label)

ngramfeatures=[]
trainfeatures,testfeatures,lexicon=bulkBagOfWords(trainitems, testitems)
ngramfeatures.append(trainfeatures,testfeatures,lexicon)
for n in range(1,4):
	train,test,lexicon=bulkNgrams(trainitems,testitems,n)
	ngramfeatures.append((train,test, lexicon))

clf = svm.SVC()
clf.fit(trainfeatures,trainlabels)
