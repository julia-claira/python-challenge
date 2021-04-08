#import needed modules
import re
import os

#---declare variables------
theWords=[] #stores the individual words in array
wordCount=0 #count of the words
theSentences=[] #stores the sentences in array
sentenceCount=0 #count of the sentences
totalLetters=0 #counts the letters in all the words
averageWordLen="" #the average number of letters per word
averageSen_Len="" #the average sentence length

#----open the text file to analyze---------
textpath=os.path.join("Resources","my_paragraph.txt")
theParagraph=open(textpath,"r")


#reads the paragraph and stores and counts sentences and words into arrays
for row in theParagraph:
    theWords=re.findall("\w+", row) #parses words into an array
    wordCount=len(theWords) #counts the words
    theSentences = re.split("(?<=[.!?]) +", row)
    sentenceCount = len(theSentences) #count of sentences

#finds the average letter count---------
for i in theWords:
    totalLetters=totalLetters+len(i)

averageWordLen = str(round(totalLetters/wordCount,2)) #finds the average


#output the final results-----------------
print()
print("Paragraph Analysis")
print("------------------")
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count:" + str(sentenceCount))
print("Average Letter Count:" + averageWordLen)
print("Average Sentence Length: " + str(round(wordCount/sentenceCount,0)))
print()
