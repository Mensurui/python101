import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "IF GOD DIDNT EXIST WE SHOULD HAVE TO CREATE IT"

print(word_tokenize(text))

print(nltk.tokenize.sent_tokenize(text))

#I didnt understand this part of the code
stopwords = stopwords.words('english')
new_text = []
for i in text.split():
    if i not in stopwords: 
        new_text.append(i)
        
print(new_text)