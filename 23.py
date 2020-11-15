# Aiyush Gupta 10ST
# String Manipulation
# Task 23
# NLTK

import nltk
import ssl
import passage

#ssl._create_default_https_context = ssl._create_unverified_context
#nltk.download()
passage = passage.text.lower()
passage = passage.replace(",", "")
passage = passage.replace("-", "")
passage = passage.replace(".", "")

text = nltk.word_tokenize(passage)
tagged_text=nltk.pos_tag(text)


for x in tagged_text:
    print(*x)

print ("\n")
nltk.help.upenn_tagset('NN')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('DT')
nltk.help.upenn_tagset('RB')
nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('VBN')
nltk.help.upenn_tagset('JJS')
nltk.help.upenn_tagset('NNS')
