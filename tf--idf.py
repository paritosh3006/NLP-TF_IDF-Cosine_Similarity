#!/usr/bin/env python
# coding: utf-8

# In[1]:


print "hi"


# In[2]:


docA= "I am going to bangalore"
docB= "I am coming from Delhi"


# In[6]:


bowA= docA.split (" ")   # split document in corpus in each word
bowB= docB.split (" ")


# In[7]:


bowA       #represent a document


# In[8]:


bowB


# In[9]:


# create a vector of all possible words. and count how many times each word appears

wordSet= set(bowA).union(set(bowB))


# In[10]:


wordSet


# In[11]:


wordDictA= dict.fromkeys(wordSet,0)
wordDictB= dict.fromkeys(wordSet,0) 


# In[12]:


wordDictA


# In[13]:


wordDictB


# In[14]:


#count the words in bags:

for word in bowA:
    wordDictA[word]+=1
for word in bowB:
    wordDictB[word]+=1


# In[15]:


wordDictA


# In[17]:


import pandas as pd
pd.DataFrame([wordDictA,wordDictB])


# In[52]:


# using tf- idf


def computeTF(wordDict,bow):
    tfDict= {}
    bowCount= len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict


# In[53]:


#cal term frequency of BowA and B

tfBowA= computeTF(wordDictA, bowA)
tfBowB= computeTF(wordDictB, bowB)


# In[54]:


def computeIDF(docList):
    import math
    idfDict= {}
    N= len(docList)
    
# count the number of documents that contain a word

    idfDict= dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            
            if val> 0:
                idfDict[word] +=1
# divide N by denominator

    for word, val in idfDict.iteritems():
        idfDict[word]= math.log(N / float(val))
        
    return idfDict


# In[55]:


idfs= computeIDF([wordDictA, wordDictB])


# In[56]:


def computeTFIDF(tfBow,idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word]= val * idfs[word]
    return tfidf


# In[63]:


tfidfBowA= computeTFIDF(tfBowA,idfs)
tfidfBowB= computeTFIDF(tfBowB,idfs)


# In[64]:


import pandas as pd
pd.DataFrame([tfidfBowA, tfidfBowB])


# In[ ]:




