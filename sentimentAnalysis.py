import pandas as pd
import textblob
from textblob import TextBlob
#Language Detection using another Python package 'langdetect'
from langdetect import detect
#translator
from deep_translator import GoogleTranslator

#The sentiment function in TextBlob returns a sentiment tuple of the form (polarity, subjectivity).
# The polarity score is a float within the range [-1.0, 1.0].  -1 indicates negative sentiment and
# +1 indicates positive sentiments.The subjectivity is a float within the
# range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective
#load public questions df (save as utf-8 tab)
#
detect(u"后来恋爱被老师谈话没收手机对老师极度反感。")
#
df = pd.read_excel('C:/Users/dsl89/Documents/spring24/gradAssistant/testPython/workplace/placeholder.xlsx', sheet_name = 0)
df2 = df.iloc[0:,1]      #pub consultant question
df2
# saving the dataframe
#df2[0:, 1].to_csv('file1.csv')

#questions list
questions = []
# loop to access questions
for i in df2:
    # translate
    translated = GoogleTranslator(source='zh-CN', target='en').translate(i)
    questions.append(translated)
    #print(i)

for k in questions:         #slow view
    print(k)


blobList = [] #list to store blobs
for j in questions:
    #print(j)
    blob = TextBlob(j)
    subjectivity = blob.sentiment
    blobList.append(subjectivity[1])       # just subjectivity, not polarity

for m in blobList:
    print(m)


# Done individually
text = """
大佬你好，我想咨询您一个简单（对您而言应该很简单的两道题），关于运放应用电路设计问题，最近要做这个研学，我做了半天都是错的😫😫但我很想知道这个怎么写。。

"""
translated = GoogleTranslator(source='zh-CN', target='en').translate(text)
translated
blob = TextBlob(translated)
subjectivity = blob.sentiment[1]
subjectivity


# translate
# translated = GoogleTranslator(source='zh-CN', target='en').translate(text)
# translated
#
# blob = TextBlob(translated)
# blob.sentiment_assessments
# blob.tags
# blob.noun_phrases
# subjectivity = blob.sentiment[1]
# subjectivity
# blob.sentences
# blob.polarity
# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)




